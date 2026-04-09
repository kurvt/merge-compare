# 合入对比工具 · Merge Compare Tool

对比 **BSP** (`bsp_REL1_CSP1_20260219`) 与 **STR** (`bsp_str_debug`) 分支合入情况，支持多人协作标记。

## 快速部署到 Streamlit Community Cloud

### 1. 上传到 GitHub

```bash
# 在 GitHub 创建一个新的公开仓库（如 merge-compare），然后：
cd merge-compare-app
git init
git add .
git commit -m "init: merge compare tool"
git remote add origin https://github.com/你的用户名/merge-compare.git
git push -u origin main
```

### 2. 部署到 share.streamlit.io

1. 打开 https://share.streamlit.io/
2. 点击 **New app**
3. 选择你的 GitHub 仓库
4. Main file path 填写：`app.py`
5. 点击 **Deploy!**

部署完成后会得到一个公开链接，团队成员直接打开即可使用。

---

## 本地运行

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 多人协作说明

基于 `@st.cache_resource` 进程级单例，**所有打开同一链接的用户共享同一份勾选状态**。

**协作流程：**

1. 把 Streamlit 部署链接发给团队成员
2. 每人输入自己的昵称，直接在表格中打勾
3. 其他人点击左侧 **🔄 刷新获取最新状态** 即可看到别人的勾选

> ⚠️ 服务器因长时间无人访问休眠重启后状态会重置（Streamlit Cloud 免费版约 7 天无访问后休眠）。
> 需要持久化时，用 **📤 导出** 保存 JSON，下次重启后 **📥 导入** 恢复。

---

## 文件结构

```
merge-compare-app/
├── app.py              # 主应用（Streamlit 入口）
├── data_parser.py      # 数据解析与相似度匹配
├── builtin_data.py     # 内置示例数据（BSP + STR 原始记录）
├── requirements.txt    # Python 依赖
└── .streamlit/
    └── config.toml     # 主题配置
```

## 功能说明

| 功能 | 说明 |
|------|------|
| ✅ 勾选标记 | 表格第一列复选框，标记已合入 |
| 🔀 自动匹配 | 按 Subject 描述相似度匹配（精确/相似/无匹配） |
| 👤 作者过滤 | 下拉选择任意作者 |
| ⏱ 排序 | 支持按时间/作者/大小/匹配度 |
| 🔍 全文搜索 | 实时搜索 Subject/JiraNo/作者/仓库 |
| 📊 统计进度 | 顶部数字卡片 + 进度条 |
| 📤 导出状态 | 导出 JSON 供他人导入同步 |
| 📋 三视图 | BSP分支 / STR分支 / 对比视图 |
