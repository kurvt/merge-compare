"""
BSP vs STR 合并记录对比工具
多用户共享状态版（share.streamlit.io）
"""
import streamlit as st
import pandas as pd
from datetime import datetime
from typing import Optional

from builtin_data import BSP_DATA
from data_parser import load_from_json

st.set_page_config(page_title="BSP-STR 合并对比", layout="wide")

# ────────────────────────────────────────────
# 进程级共享状态（多用户共享同一份数据）
# ────────────────────────────────────────────
@st.cache_resource
def get_global_state():
    bsp = load_from_json(BSP_DATA)
    return {
        "bsp":          bsp,
        "checked":      {},
        "last_updated": None,
    }

G = get_global_state()

# ────────────────────────────────────────────
# 工具函数
# ────────────────────────────────────────────
def set_checked(idx: str, val: bool):
    G["checked"][idx] = val
    G["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def build_df(filters: dict) -> pd.DataFrame:
    rows = []
    for item in G["bsp"]:
        if filters.get("author") and item.get("author") != filters["author"]:
            continue
        if filters.get("repo") and item.get("repo") != filters["repo"]:
            continue
        if filters.get("ctype") and item.get("commit_type") != filters["ctype"]:
            continue
        idx        = item["idx"]
        checked    = G["checked"].get(idx, item.get("in_str", False))
        status_lbl = "✅ 已合入" if item.get("in_str") else "❌ 未合入"
        rows.append({
            "已确认":  bool(checked),
            "JIRA":    item.get("jira_no", ""),
            "主题":    item.get("subject", ""),
            "类型":    item.get("commit_type", ""),
            "模块":    item.get("function", ""),
            "仓库":    item.get("repo", ""),
            "作者":    item.get("author", ""),
            "STR状态": status_lbl,
            "_idx":    idx,
        })
    return pd.DataFrame(rows)


# ────────────────────────────────────────────
# 界面
# ────────────────────────────────────────────
st.title("BSP → STR 合并记录对比")

# 侧边栏
with st.sidebar:
    st.header("筛选条件")

    authors = sorted({x.get("author", "") for x in G["bsp"] if x.get("author")})
    author_sel = st.selectbox("作者", ["全部"] + authors)

    repos = sorted({x.get("repo", "") for x in G["bsp"] if x.get("repo")})
    repo_sel = st.selectbox("仓库", ["全部"] + repos)

    ctypes = sorted({x.get("commit_type", "") for x in G["bsp"] if x.get("commit_type")})
    ctype_sel = st.selectbox("提交类型", ["全部"] + ctypes)

    filters = {
        "author": None if author_sel == "全部" else author_sel,
        "repo":   None if repo_sel   == "全部" else repo_sel,
        "ctype":  None if ctype_sel  == "全部" else ctype_sel,
    }

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 刷新"):
            st.rerun()
    with col2:
        if st.button("🗑️ 重置所有"):
            G["checked"].clear()
            st.rerun()

    st.divider()
    total   = len(G["bsp"])
    in_str  = sum(1 for x in G["bsp"] if x.get("in_str"))
    checked = sum(1 for x in G["bsp"] if G["checked"].get(x["idx"], x.get("in_str", False)))
    st.metric("总条数",  total)
    st.metric("STR已有", in_str,  delta=f"{in_str/total*100:.1f}%")
    st.metric("已确认",  checked, delta=f"{checked/total*100:.1f}%")

    if G["last_updated"]:
        st.caption(f"最后更新: {G['last_updated']}")

    st.divider()
    df_exp = build_df({})
    st.download_button(
        "📥 导出CSV",
        df_exp.drop(columns=["_idx"]).to_csv(index=False).encode(),
        "bsp_str_compare.csv",
        "text/csv",
    )


# ────────────────────────────────────────────
# Fragment：勾选时只刷新表格，不滚回顶部
# ────────────────────────────────────────────
@st.fragment
def render_table(tab_key: str, f_val, filters: dict):
    df = build_df(filters)
    if f_val is True:
        df = df[df["已确认"] == True]
    elif f_val is False:
        df = df[df["已确认"] == False]

    if df.empty:
        st.info("暂无数据")
        return

    edited = st.data_editor(
        df.drop(columns=["_idx"]),
        column_config={
            "已确认":  st.column_config.CheckboxColumn("已确认", default=False),
            "JIRA":    st.column_config.TextColumn("JIRA",    width="small"),
            "主题":    st.column_config.TextColumn("主题",    width="large"),
            "类型":    st.column_config.TextColumn("类型",    width="small"),
            "模块":    st.column_config.TextColumn("模块",    width="small"),
            "仓库":    st.column_config.TextColumn("仓库",    width="medium"),
            "作者":    st.column_config.TextColumn("作者",    width="small"),
            "STR状态": st.column_config.TextColumn("STR状态", width="small"),
        },
        use_container_width=True,
        hide_index=True,
        key=f"editor_{tab_key}",
    )

    changed = False
    for (_, row_orig), (_, row_edit) in zip(df.iterrows(), edited.iterrows()):
        if row_orig["已确认"] != row_edit["已确认"]:
            idx = df.loc[row_orig.name, "_idx"]
            set_checked(idx, bool(row_edit["已确认"]))
            changed = True
    if changed:
        st.rerun(scope="fragment")  # 只重渲染本片段，不滚回顶部


# 主视图
tab_all, tab_in, tab_out = st.tabs(["📋 全部", "✅ 已合入", "❌ 未合入"])
with tab_all:
    render_table("all",  None,  filters)
with tab_in:
    render_table("in",   True,  filters)
with tab_out:
    render_table("out",  False, filters)
