"""
BSP vs STR 合并记录对比工具
多用户共享状态版（share.streamlit.io）
"""
import streamlit as st
import pandas as pd
from datetime import datetime
from typing import Optional

from builtin_data import BSP_DATA
from data_parser import load_from_json, parse_pipe_text

st.set_page_config(page_title="BSP-STR 合并对比", layout="wide")

# ────────────────────────────────────────────
# 进程级共享状态（多用户共享同一份数据）
# ────────────────────────────────────────────
@st.cache_resource
def get_global_state():
    bsp = load_from_json(BSP_DATA)
    return {
        "bsp":          bsp,
        "checked":      {},      # { idx -> bool }
        "last_updated": None,
        "update_by":    "",
    }

G = get_global_state()

# ────────────────────────────────────────────
# 工具函数
# ────────────────────────────────────────────
def set_checked(idx: str, val: bool, user: str):
    G["checked"][idx] = val
    G["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    G["update_by"] = user

def build_df(author_filter: Optional[str]) -> pd.DataFrame:
    rows = []
    for item in G["bsp"]:
        if author_filter and item.get("author") != author_filter:
            continue
        idx        = item["idx"]
        checked    = G["checked"].get(idx, item.get("in_str", False))
        status_lbl = "✅ 已合入" if item.get("in_str") else "❌ 未合入"
        rows.append({
            "已确认": bool(checked),
            "JIRA":   item.get("jira_no", ""),
            "主题":   item.get("subject", ""),
            "类型":   item.get("commit_type", ""),
            "模块":   item.get("function", ""),
            "仓库":   item.get("repo", ""),
            "作者":   item.get("author", ""),
            "STR状态": status_lbl,
            "_idx":   idx,
        })
    return pd.DataFrame(rows)

# ────────────────────────────────────────────
# 界面
# ────────────────────────────────────────────
st.title("BSP → STR 合并记录对比")

# 侧边栏
with st.sidebar:
    st.header("控制面板")
    nickname = st.text_input("你的昵称", value="anonymous", key="nick")

    authors = sorted({x.get("author","") for x in G["bsp"] if x.get("author")})
    author_sel = st.selectbox("按作者筛选", ["全部"] + authors)
    author_filter: Optional[str] = None if author_sel == "全部" else author_sel

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
    st.metric("总条数",   total)
    st.metric("STR已有",  in_str,  delta=f"{in_str/total*100:.1f}%")
    st.metric("已确认",   checked, delta=f"{checked/total*100:.1f}%")

    if G["last_updated"]:
        st.caption(f"最后更新: {G['last_updated']} by {G['update_by']}")

    st.divider()
    # 导出
    df_exp = build_df(None)
    st.download_button("📥 导出CSV", df_exp.drop(columns=["_idx"]).to_csv(index=False).encode(),
                       "bsp_str_compare.csv", "text/csv")

# 主视图
tabs = st.tabs(["📋 全部", "✅ 已合入", "❌ 未合入"])
filters = [None, True, False]  # None = 全部, True = 已确认, False = 未确认

for tab, f_val in zip(tabs, filters):
    with tab:
        df = build_df(author_filter)
        if f_val is True:
            df = df[df["已确认"] == True]
        elif f_val is False:
            df = df[df["已确认"] == False]

        if df.empty:
            st.info("暂无数据")
            continue

        edited = st.data_editor(
            df.drop(columns=["_idx"]),
            column_config={
                "已确认": st.column_config.CheckboxColumn("已确认", default=False),
                "JIRA":   st.column_config.TextColumn("JIRA", width="small"),
                "主题":   st.column_config.TextColumn("主题", width="large"),
                "类型":   st.column_config.TextColumn("类型", width="small"),
                "模块":   st.column_config.TextColumn("模块", width="small"),
                "仓库":   st.column_config.TextColumn("仓库", width="medium"),
                "作者":   st.column_config.TextColumn("作者", width="small"),
                "STR状态": st.column_config.TextColumn("STR状态", width="small"),
            },
            use_container_width=True,
            hide_index=True,
            key=f"editor_{f_val}_{author_sel}",
        )

        # 检测勾选状态变化并写回共享状态
        changed = False
        for (_, row_orig), (_, row_edit) in zip(df.iterrows(), edited.iterrows()):
            if row_orig["已确认"] != row_edit["已确认"]:
                idx = df.loc[row_orig.name, "_idx"]
                set_checked(idx, bool(row_edit["已确认"]), nickname)
                changed = True
        if changed:
            st.rerun()
