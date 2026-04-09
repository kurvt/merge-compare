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

# 确认状态选项
STATUS_OPTIONS = ["--", "STR已合入", "重复/无效"]

# ────────────────────────────────────────────
# 进程级共享状态
# ────────────────────────────────────────────
@st.cache_resource
def get_global_state():
    bsp = load_from_json(BSP_DATA)
    # 初始化：in_str=True 的默认标为 "STR已合入"
    status = {}
    for item in bsp:
        if item.get("in_str"):
            status[item["idx"]] = "STR已合入"
    return {
        "bsp":          bsp,
        "status":       status,   # { idx -> "STR已合入" | "重复/无效" | "--" }
        "last_updated": None,
    }

G = get_global_state()


def get_status(idx: str, in_str: bool) -> str:
    return G["status"].get(idx, "STR已合入" if in_str else "--")


def build_df(filters: dict) -> pd.DataFrame:
    rows = []
    for item in G["bsp"]:
        if filters.get("author") and item.get("author") != filters["author"]:
            continue
        if filters.get("repo") and item.get("repo") != filters["repo"]:
            continue
        if filters.get("ctype") and item.get("commit_type") != filters["ctype"]:
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
            "STR状态": "✅ 已合入" if item.get("in_str") else "❌ 未合入",
            "_idx":    idx,
        })
    return pd.DataFrame(rows)


# ────────────────────────────────────────────
# 界面
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
            G["status"].clear()
            st.rerun()

    st.divider()
    total    = len(G["bsp"])
    n_merged = sum(1 for x in G["bsp"] if get_status(x["idx"], x.get("in_str", False)) == "STR已合入")
    n_dup    = sum(1 for x in G["bsp"] if get_status(x["idx"], x.get("in_str", False)) == "重复/无效")
    n_todo   = total - n_merged - n_dup
    st.metric("总条数",       total)
    st.metric("STR已合入",    n_merged, delta=f"{n_merged/total*100:.0f}%")
    st.metric("重复/无效",    n_dup,    delta=f"{n_dup/total*100:.0f}%")
    st.metric("待确认",       n_todo,   delta=f"{n_todo/total*100:.0f}%")

    if G["last_updated"]:
        st.caption(f"最后更新: {G['last_updated']}")

    st.divider()
    df_exp = build_df({})
    st.download_button(
        "📥 导出CSV",
        df_exp.drop(columns=["_idx"]).to_csv(index=False).encode(),
        "bsp_str_compare.csv", "text/csv",
    )

# ────────────────────────────────────────────
# 回调：data_editor on_change，静默写入不 rerun
# ────────────────────────────────────────────
def sync_edits(tab_key: str, df: pd.DataFrame):
    """从 session_state 中读取 data_editor 的编辑结果并写入全局状态"""
    key = f"editor_{tab_key}"
    if key not in st.session_state:
        return
    state = st.session_state[key]
    edited_rows = state.get("edited_rows", {})
    for row_str, changes in edited_rows.items():
        row_idx = int(row_str)
        if "确认状态" in changes and row_idx < len(df):
            idx = df.iloc[row_idx]["_idx"]
            G["status"][idx] = changes["确认状态"]
            G["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ────────────────────────────────────────────
# 渲染表格（@st.fragment 隔离，避免整页刷新）
# ────────────────────────────────────────────
@st.fragment
def render_table(tab_key: str, show_filter, filters: dict):
    df = build_df(filters)
    if show_filter == "confirmed":
        df = df[df["确认状态"] != "--"]
    elif show_filter == "todo":
        df = df[df["确认状态"] == "--"]
    df = df.reset_index(drop=True)

    if df.empty:
        st.info("暂无数据")
        return

    # 先同步上次编辑（on_change 触发时 session_state 已更新）
    sync_edits(tab_key, df)

    st.data_editor(
        df.drop(columns=["_idx"]),
        column_config={
            "确认状态": st.column_config.SelectboxColumn(
                "确认状态", options=STATUS_OPTIONS, width="small", required=True,
            ),
            "JIRA":    st.column_config.TextColumn("JIRA",    width="small"),
            "主题":    st.column_config.TextColumn("主题",    width="large"),
            "类型":    st.column_config.TextColumn("类型",    width="small"),
            "模块":    st.column_config.TextColumn("模块",    width="small"),
            "仓库":    st.column_config.TextColumn("仓库",    width="medium"),
            "作者":    st.column_config.TextColumn("作者",    width="small"),
            "STR状态": st.column_config.TextColumn("STR状态", width="small"),
        },
        disabled=["JIRA", "主题", "类型", "模块", "仓库", "作者", "STR状态"],
        use_container_width=True,
        hide_index=True,
        key=f"editor_{tab_key}",
    )

tab_all, tab_done, tab_todo = st.tabs(["📋 全部", "✅ 已确认", "❓ 待确认"])
with tab_all:
    render_table("all",  None,        filters)
with tab_done:
    render_table("done", "confirmed", filters)
with tab_todo:
    render_table("todo", "todo",      filters)
