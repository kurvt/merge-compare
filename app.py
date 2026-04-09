"""
BSP vs STR 合并记录对比工具
多用户共享状态版（share.streamlit.io）
"""
import streamlit as st
import pandas as pd
from datetime import datetime

from builtin_data import BSP_DATA
from data_parser import load_from_json

st.set_page_config(page_title="BSP-STR 合并对比", layout="wide")

S_TODO    = "🔴 待确认"
S_MERGED  = "🟢 STR已合入"
S_INVALID = "🟡 重复/无效"
STATUS_OPTIONS = [S_TODO, S_MERGED, S_INVALID]

ROW_HEIGHT = 35

# ────────────────────────────────────────────
# 进程级共享状态
# ────────────────────────────────────────────
@st.cache_resource
def get_global_state():
    bsp = load_from_json(BSP_DATA)
    status = {}
    for item in bsp:
        if item.get("in_str"):
            status[item["idx"]] = S_MERGED
    return {
        "bsp":          bsp,
        "status":       status,
        "last_updated": None,
    }

G = get_global_state()


def get_status(idx, in_str=False):
    return G["status"].get(idx, S_MERGED if in_str else S_TODO)


def build_rows(filters):
    rows = []
    for item in G["bsp"]:
        if filters.get("author") and item.get("author") != filters["author"]:
            continue
        if filters.get("repo") and item.get("repo") != filters["repo"]:
            continue
        if filters.get("ctype") and item.get("commit_type") != filters["ctype"]:
            continue
        if filters.get("updated") and item.get("updated") != filters["updated"]:
            continue
        idx = item["idx"]
        rows.append({
            "确认状态": get_status(idx, item.get("in_str", False)),
            "JIRA":    item.get("jira_no", ""),
            "主题":    item.get("subject", ""),
            "类型":    item.get("commit_type", ""),
            "模块":    item.get("function", ""),
            "仓库":    item.get("repo", ""),
            "作者":    item.get("author", ""),
            "时间":    item.get("updated", ""),
            "_idx":    idx,
        })
    return rows


# ────────────────────────────────────────────
# 侧边栏
# ────────────────────────────────────────────
st.title("BSP → STR 合并记录对比")

with st.sidebar:
    st.header("筛选条件")

    authors = sorted({x.get("author", "") for x in G["bsp"] if x.get("author")})
    author_sel = st.selectbox("作者", ["全部"] + authors)

    repos = sorted({x.get("repo", "") for x in G["bsp"] if x.get("repo")})
    repo_sel = st.selectbox("仓库", ["全部"] + repos)

    ctypes = sorted({x.get("commit_type", "") for x in G["bsp"] if x.get("commit_type")})
    ctype_sel = st.selectbox("提交类型", ["全部"] + ctypes)

    # 时间筛选 - 按时间倒序排列
    def time_sort_key(t):
        months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,
                   'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        parts = t.split()
        if len(parts) == 2 and parts[0] in months:
            return (months[parts[0]], int(parts[1]))
        return (0, 0)

    times = sorted(
        {x.get("updated", "") for x in G["bsp"] if x.get("updated")},
        key=time_sort_key, reverse=True,
    )
    time_sel = st.selectbox("时间", ["全部"] + times)

    filters = {
        "author":  None if author_sel == "全部" else author_sel,
        "repo":    None if repo_sel   == "全部" else repo_sel,
        "ctype":   None if ctype_sel  == "全部" else ctype_sel,
        "updated": None if time_sel   == "全部" else time_sel,
    }

    if st.button("🗑️ 重置所有确认"):
        G["status"].clear()
        for item in G["bsp"]:
            if item.get("in_str"):
                G["status"][item["idx"]] = S_MERGED
        st.rerun()

    st.divider()
    total    = len(G["bsp"])
    n_merged = sum(1 for x in G["bsp"] if get_status(x["idx"], x.get("in_str", False)) == S_MERGED)
    n_dup    = sum(1 for x in G["bsp"] if get_status(x["idx"], x.get("in_str", False)) == S_INVALID)
    n_todo   = total - n_merged - n_dup
    st.metric("总条数",    total)
    st.metric("🟢 STR已合入", n_merged, delta=f"{n_merged/total*100:.0f}%")
    st.metric("🟡 重复/无效", n_dup,    delta=f"{n_dup/total*100:.0f}%")
    st.metric("🔴 待确认",    n_todo,   delta=f"{n_todo/total*100:.0f}%")
    if G["last_updated"]:
        st.caption(f"最后更新: {G['last_updated']}")

    st.divider()
    all_rows_exp = build_rows({})
    df_exp = pd.DataFrame(all_rows_exp).drop(columns=["_idx"])
    st.download_button("📥 导出CSV", df_exp.to_csv(index=False).encode(),
                       "bsp_str_compare.csv", "text/csv")


# ────────────────────────────────────────────
# 渲染表格 + st.form 批量保存
# ────────────────────────────────────────────
def render_table(tab_key, show_filter, filters):
    all_rows = build_rows(filters)
    if show_filter == "confirmed":
        all_rows = [r for r in all_rows if r["确认状态"] != S_TODO]
    elif show_filter == "todo":
        all_rows = [r for r in all_rows if r["确认状态"] == S_TODO]

    n_total = len(all_rows)
    if n_total == 0:
        st.info("暂无数据")
        return

    st.caption(f"共 {n_total} 条")
    df = pd.DataFrame(all_rows).reset_index(drop=True)

    editor_key = f"editor_{tab_key}"
    table_height = (n_total + 1) * ROW_HEIGHT + 3

    with st.form(key=f"form_{tab_key}"):
        edited = st.data_editor(
            df.drop(columns=["_idx"]),
            column_config={
                "确认状态": st.column_config.SelectboxColumn(
                    "确认状态", options=STATUS_OPTIONS, width="small", required=True,
                ),
                "JIRA":  st.column_config.TextColumn("JIRA",  width="small"),
                "主题":  st.column_config.TextColumn("主题",  width="large"),
                "类型":  st.column_config.TextColumn("类型",  width="small"),
                "模块":  st.column_config.TextColumn("模块",  width="small"),
                "仓库":  st.column_config.TextColumn("仓库",  width="medium"),
                "作者":  st.column_config.TextColumn("作者",  width="small"),
                "时间":  st.column_config.TextColumn("时间",  width="small"),
            },
            disabled=["JIRA", "主题", "类型", "模块", "仓库", "作者", "时间"],
            use_container_width=True,
            hide_index=True,
            height=table_height,
            key=editor_key,
        )
        submitted = st.form_submit_button("💾 保存所有修改", use_container_width=True, type="primary")

    if submitted:
        n_changed = 0
        for i, row in edited.iterrows():
            idx = df.iloc[i]["_idx"]
            new_val = row["确认状态"]
            old_val = df.iloc[i]["确认状态"]
            if new_val != old_val:
                G["status"][idx] = new_val
                n_changed += 1
        if n_changed > 0:
            G["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.success(f"已保存 {n_changed} 条修改")
        else:
            st.info("没有需要保存的修改")


# ────────────────────────────────────────────
# 主视图
# ────────────────────────────────────────────
tab_all, tab_done, tab_todo = st.tabs(["📋 全部", "🟢 已确认", "🔴 待确认"])
with tab_all:
    render_table("all",  None,        filters)
with tab_done:
    render_table("done", "confirmed", filters)
with tab_todo:
    render_table("todo", "todo",      filters)
