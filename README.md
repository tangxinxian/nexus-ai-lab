# Nexus AI Lab

Nexus AI Lab 是 AI 应用开发工程师实习训练项目的公共技术底座，用于沉淀 Prompt 模板、模型调用封装、结构化输出、工具调用示例和 FastAPI AI 服务。

本项目将作为后续三个 Nexus 项目的公共能力层：

- Nexus Research：AI 行业研究与情报分析平台
- Nexus Dev：AI 代码理解与研发协作平台
- Nexus Agent：多智能体任务编排平台

## 项目定位

本项目的目标不是训练大模型，而是学习如何将大模型能力集成到真实应用中，形成可复用、可运行、可展示的 AI 应用开发能力。

核心训练内容包括：

- Prompt Engineering
- LLM API 调用封装
- Structured Output
- Function Calling / Tool Calling
- FastAPI AI 服务封装
- 项目文档、开发日志与 Demo 展示

## W1 学习目标

- 理解 Prompt Engineering 的核心范式：角色设定、任务拆解、输入约束、输出格式、Few-shot、错误修正
- 掌握 LLM API 的基本调用方式：Chat、Streaming、Structured Output、Function Calling / Tool Calling
- 使用 Python 构建最小 AI 服务：FastAPI + Pydantic + 环境变量管理 + 简单错误处理
- 形成工程化习惯：README、运行截图、接口文档、开发日志
- 为 Nexus 三大项目沉淀通用组件：模型调用封装、Prompt 模板、配置管理、基础接口

## 项目结构

```text
Nexus/
├── apps/                  应用入口，例如 FastAPI 服务
├── packages/              可复用代码模块，例如模型客户端、工具函数
├── prompts/               Prompt 模板库
├── docs/                  项目文档
│   ├── plans/             实习计划、周计划、路线图等规划类文档
│   ├── logs/              每日开发日志
│   ├── notes/             学习笔记
│   ├── images/            环境截图、接口截图、运行截图
│   └── demos/             Demo 说明、录屏链接、展示素材
├── .python-version        uv 固定的 Python 版本
├── .gitignore             Git 忽略规则
├── README.md              项目说明文档
└── requirements.txt       Python 依赖列表
```

## 文档说明

- `docs/plans/`：项目规划文档，使用 Markdown 格式方便 GitHub 在线阅读
- `docs/logs/`：每日开发日志，记录每日目标、完成内容、问题与复盘
- `docs/notes/`：学习笔记，记录 Prompt、API、FastAPI、Pydantic 等知识点
- `docs/images/`：环境截图、运行截图、接口截图
- `docs/demos/`：Demo 说明、录屏链接、展示素材

## 环境准备

本项目使用 `uv` 管理 Python 版本和虚拟环境。

### 创建环境

```powershell
uv python pin 3.11
uv venv
.venv\Scripts\activate
uv pip install openai python-dotenv fastapi uvicorn pydantic
uv pip freeze > requirements.txt
```

### 验证环境

```powershell
python --version
python -c "import openai, fastapi, pydantic; print('env ok')"
```

预期输出：

```text
Python 3.11.14
env ok
```

## Git 使用记录

当前项目已完成：

- 本地 Git 仓库初始化
- 第一次项目结构提交
- 远程 GitHub 仓库绑定
- 首次推送到 GitHub

第一次提交记录：

```text
7ccd0b0 init nexus ai lab project structure
```

## 当前进度

- [x] D1：项目定位与环境搭建
- [ ] D2：Prompt 基础
- [ ] D3：结构化输出
- [ ] D4：LLM API 调用封装
- [ ] D5：Function Calling
- [ ] D6：FastAPI AI 服务
- [ ] D7：复盘与包装

## W1 交付清单

- [x] GitHub 仓库：包含清晰 README 和基础运行方式
- [ ] Prompt 模板库：至少 9 个 Prompt，覆盖总结、抽取、分类、任务拆解、代码解释
- [ ] 模型调用封装：ModelClient 支持普通调用、流式输出、异常处理
- [ ] FastAPI Demo：提供 `/chat`、`/summarize`、`/plan` 三个接口
- [x] 开发日志：记录每天学到的内容、遇到的问题和解决方案
- [ ] Demo 素材：至少 3 张截图或 1 分钟录屏，为后续简历和面试准备素材

## 后续计划

D2 将进入 Prompt 基础学习，重点完成：

- 角色设定 Prompt
- 任务边界 Prompt
- 输入输出约束 Prompt
- Few-shot 示例
- 行业信息总结、代码解释、任务拆解三类 Prompt 模板