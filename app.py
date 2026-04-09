#!/usr/bin/env python3
"""
合入对比工具 - Streamlit 版本
多人共享：基于 @st.cache_resource 进程级单例，所有用户打开同一链接即协作。
"""

import streamlit as st
import json
import pandas as pd
from datetime import datetime

from data_parser import parse_raw_text, enrich_with_matches
from builtin_data import BSP_BUILTIN, STR_BUILTIN

# ==================== 页面配置 ====================
st.set_page_config(
    page_title="合入对比 BSP↔STR",
    page_icon="🔀",
    layout="wide",
)

# ==================== 共享全局状态（跨所有用户 session） ====================
@st.cache_resource
def get_global_state():
    """
    进程级单例，Streamlit Community Cloud 单实例部署时所有 session 共用。
    服务器因长时间无访问休眠重启后会重置，但对低实时性协作完全够用。
    """
    bsp_list = parse_raw_text(BSP_BUILTIN)
    str_list = parse_raw_text(STR_BUILTIN)
    return {
        "bsp_data": enrich_with_matches(bsp_list, str_list, "bsp"),
        "str_data": enrich_with_matches(str_list, bsp_list, "str"),
        "checked": {},
        "last_updated": None,
        "update_by": "",
    }

G = get_global_state()

# ==================== CSS ====================
st.markdown("""
<style>
.block-container { padding-top: 1rem !important; }
div[data-testid="metric-container"] {
    background: #f8f9fa; border-radius: 8px; padding: 8px 14px;
}
</style>
""", unsafe_allow_html=True)

# ==================== Session 私有状态 ====================
if "nickname" not in st.session_state:
    st.session_state.nickname = ""

# ==================== 工具函数 ====================
SIZE_ORDER = {"--": 0, "XS": 1, "S": 2, "M": 3, "L": 4, "XL": 5}
MATCH_LABELS = {"exact": "✅ 精确匹配", "similar": "🟡 相似匹配", "none": "— 无匹配"}

def get_checked(idx):
    return G["checked"].get(idx, False)

def set_checked(idx, val, who=""):
    G["checked"][idx] = val
    G["last_updated"] = datetime.now()
    G["update_by"] = who

def batch_set(indices, val, who=""):
    for idx in indices:
        G["checked"][idx] = val
    G["last_updated"] = datetime.now()
    G["update_by"] = who

def filter_and_sort(data, author_f, status_f, match_f, search, sort_field, sort_asc):
    result = list(data)
    if author_f:
        result = [d for d in result if d.get("author") == author_f]
    if status_f == "已勾选":
        result = [d for d in result if get_checked(d["idx"])]
    elif status_f == "未勾选":
        result = [d for d in result if not get_checked(d["idx"])]
    if match_f and match_f != "全部":
        key = {"精确匹配": "exact", "相似匹配": "similar", "无匹配": "none"}[match_f]
        result = [d for d in result if d.get("match_level") == key]
    if search:
        sl = search.lower()
        result = [d for d in result if
                  sl in (d.get("subject") or "").lower() or
                  sl in (d.get("jira_no") or "").lower() or
                  sl in (d.get("author") or "").lower() or
                  sl in (d.get("repo") or "").lower()]
    if sort_field == "时间":
        result.sort(key=lambda d: d.get("time_dt") or datetime.min, reverse=not sort_asc)
    elif sort_field == "作者":
        result.sort(key=lambda d: d.get("author") or "", reverse=not sort_asc)
    elif sort_field == "大小":
        result.sort(key=lambda d: SIZE_ORDER.get(d.get("size") or "--", 0), reverse=not sort_asc)
    elif sort_field == "匹配度":
        result.sort(key=lambda d: d.get("match_score") or 0, reverse=not sort_asc)
    return result

def stats_of(data):
    total   = len(data)
    checked = sum(1 for d in data if get_checked(d["idx"]))
    exact   = sum(1 for d in data if d.get("match_level") == "exact")
    similar = sum(1 for d in data if d.get("match_level") == "similar")
    return {"total": total, "checked": checked,
            "unchecked": total - checked, "exact": exact, "similar": similar}

# ==================== 侧边栏 ====================
with st.sidebar:
    st.header("🔀 合入对比工具")
    st.caption("BSP vs STR 分支")
    st.divider()

    nick = st.text_input("👤 你的昵称", value=st.session_state.nickname, placeholder="如: brent")
    st.session_state.nickname = nick.strip() or "匿名"

    st.divider()
    st.subheader("🔄 协作同步")
    if G["last_updated"]:
        ts = G["last_updated"].strftime("%H:%M:%S")
        st.info(f"最后更新：**{ts}**\n\n操作人：**{G['update_by']}**")
    else:
        st.info("暂无勾选记录")

    if st.button("🔄 刷新获取最新状态", use_container_width=True, type="primary"):
        st.rerun()

    st.caption("💡 同一链接的所有用户共享勾选状态。勾选后其他人点刷新即可同步。")

    st.divider()
    st.subheader("📦 导出 / 导入")
    checked_export = {k: v for k, v in G["checked"].items() if v}
    st.download_button(
        "📤 导出勾选状态 JSON",
        data=json.dumps(checked_export, ensure_ascii=False, indent=2),
        file_name="checked_state.json",
        mime="application/json",
        use_container_width=True,
    )
    imp_file = st.file_uploader("📥 导入勾选状态 (.json)", type=["json"],
                                label_visibility="collapsed")
    if imp_file:
        try:
            imported = json.loads(imp_file.read().decode("utf-8"))
            for k, v in imported.items():
                G["checked"][k] = bool(v)
            G["last_updated"] = datetime.now()
            G["update_by"] = st.session_state.nickname + "（导入）"
            st.success(f"导入 {sum(imported.values())} 条")
            st.rerun()
        except Exception as e:
            st.error(f"导入失败: {e}")

    if st.button("🗑️ 清空所有勾选", use_container_width=True):
        G["checked"].clear()
        G["last_updated"] = datetime.now()
        G["update_by"] = st.session_state.nickname + "（清空）"
        st.rerun()

# ==================== 主界面 ====================
st.title("🔀 合入对比工具")
st.caption("BSP (`bsp_REL1_CSP1_20260219`)  ↔  STR (`bsp_str_debug`)  · 多人协作")

view = st.radio("视图", ["📋 BSP 分支", "📋 STR 分支", "🔀 对比视图"],
                horizontal=True, label_visibility="collapsed")
source_key = "bsp" if "BSP" in view else ("str" if "STR" in view else "compare")

st.divider()

# ========== 过滤栏 ==========
working_data = (G["bsp_data"] if source_key == "bsp"
                else G["str_data"] if source_key == "str"
                else G["bsp_data"] + G["str_data"])

fc1, fc2, fc3, fc4, fc5, fc6 = st.columns([1.5, 1, 1, 1, 2.5, 0.8])
all_authors = sorted({d.get("author", "") for d in working_data if d.get("author")})
with fc1:
    author_f = st.selectbox("作者", [""] + all_authors,
                            format_func=lambda x: "全部作者" if x == "" else x)
with fc2:
    status_f = st.selectbox("状态", ["全部", "未勾选", "已勾选"])
with fc3:
    match_f  = st.selectbox("匹配", ["全部", "精确匹配", "相似匹配", "无匹配"])
with fc4:
    sort_field = st.selectbox("排序", ["时间", "作者", "大小", "匹配度"])
with fc5:
    search = st.text_input("🔍 搜索", placeholder="Subject / JiraNo / 作者 / 仓库...")
with fc6:
    sort_asc = st.checkbox("升序", value=False)

ba1, ba2, _, ba3 = st.columns([1, 1, 4, 1])
with ba1:
    if st.button("✅ 全部勾选（当前筛选）"):
        fd_now = filter_and_sort(working_data, author_f, status_f,
                                 match_f, search, sort_field, sort_asc)
        batch_set([d["idx"] for d in fd_now], True, st.session_state.nickname)
        st.rerun()
with ba2:
    if st.button("⬜ 全部取消（当前筛选）"):
        fd_now = filter_and_sort(working_data, author_f, status_f,
                                 match_f, search, sort_field, sort_asc)
        batch_set([d["idx"] for d in fd_now], False, st.session_state.nickname)
        st.rerun()
with ba3:
    st.caption(f"操作人：**{st.session_state.nickname}**")

st.divider()

# ========== 统计卡片 ==========
s = stats_of(G["bsp_data"])
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("📊 BSP 总条数", s["total"])
m2.metric("✅ 已勾选", s["checked"],
          delta=f"{s['checked']/s['total']*100:.0f}%" if s["total"] else None)
m3.metric("⬜ 未勾选", s["unchecked"])
m4.metric("🔵 精确匹配STR", s["exact"])
m5.metric("🟡 相似匹配", s["similar"])
if s["total"]:
    pct = s["checked"] / s["total"]
    st.progress(pct, text=f"已合入进度：{s['checked']} / {s['total']} ({pct*100:.1f}%)")

# ========== 表格渲染 ==========
def render_table(data, src_label):
    if not data:
        st.info("没有符合条件的记录")
        return
    match_col = "STR匹配" if src_label == "bsp" else "BSP匹配"
    rows = []
    for item in data:
        ml = item.get("match_level", "none")
        match_text = MATCH_LABELS.get(ml, "—")
        ms = item.get("matched_subject", "")
        if ml == "similar" and ms:
            match_text += f"  ↳ {ms[:45]}…"
        rows.append({
            "已合入":        get_checked(item["idx"]),
            "JiraNo":        item.get("jira_no", ""),
            "描述（Subject）": item.get("subject", ""),
            "作者":          item.get("author", ""),
            "时间":          item.get("time_str", ""),
            "大小":          item.get("size", "--"),
            "仓库":          item.get("repo", ""),
            match_col:       match_text,
            "_idx":          item["idx"],
        })
    df = pd.DataFrame(rows)
    edited = st.data_editor(
        df,
        column_config={
            "已合入":          st.column_config.CheckboxColumn("✅ 已合入",  width="small"),
            "JiraNo":          st.column_config.TextColumn("JiraNo",         width="small",  disabled=True),
            "描述（Subject）": st.column_config.TextColumn("描述",           width="large",  disabled=True),
            "作者":            st.column_config.TextColumn("作者",           width="small",  disabled=True),
            "时间":            st.column_config.TextColumn("时间",           width="small",  disabled=True),
            "大小":            st.column_config.TextColumn("大小",           width="small",  disabled=True),
            "仓库":            st.column_config.TextColumn("仓库",           width="medium", disabled=True),
            match_col:         st.column_config.TextColumn(match_col,        width="medium", disabled=True),
            "_idx":            st.column_config.TextColumn("_idx",           disabled=True),
        },
        hide_index=True,
        use_container_width=True,
        num_rows="fixed",
        key=f"tbl_{src_label}",
    )
    if edited is not None:
        changed = False
        for _, row in edited.iterrows():
            idx = row["_idx"]
            new_val = bool(row["已合入"])
            if get_checked(idx) != new_val:
                set_checked(idx, new_val, st.session_state.nickname)
                changed = True
        if changed:
            st.rerun()

st.divider()

if source_key == "compare":
    tab_bsp, tab_str = st.tabs([
        f"BSP 分支 ({len(G['bsp_data'])})",
        f"STR 分支 ({len(G['str_data'])})",
    ])
    with tab_bsp:
        fd = filter_and_sort(G["bsp_data"], author_f, status_f, match_f, search, sort_field, sort_asc)
        st.caption(f"显示 {len(fd)} 条")
        render_table(fd, "bsp")
    with tab_str:
        fd = filter_and_sort(G["str_data"], author_f, status_f, match_f, search, sort_field, sort_asc)
        st.caption(f"显示 {len(fd)} 条")
        render_table(fd, "str")
else:
    fd = filter_and_sort(working_data, author_f, status_f, match_f, search, sort_field, sort_asc)
    st.caption(f"显示 {len(fd)} 条 / 共 {len(working_data)} 条")
    render_table(fd, source_key)

# ========== 无匹配摘要 ==========
no_match = [d for d in G["bsp_data"]
            if d.get("match_level") == "none" and not get_checked(d["idx"])]
if no_match:
    with st.expander(f"⚠️ BSP 无匹配且未勾选（{len(no_match)} 条，可能是 STR 尚未合入）"):
        for item in no_match:
            st.markdown(
                f"- `{item.get('jira_no','?')}` **{item.get('author','')}**  "
                f"{item.get('subject','')[:80]}  "
                f"*{item.get('repo','')}* `{item.get('time_str','')}`"
            )
