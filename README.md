# Nexus AI Lab

Nexus AI Lab 是 AI 应用开发工程师实习训练项目的公共技术底座，用于沉淀 Prompt 模板、模型调用封装、工具调用示例和 FastAPI AI 服务。

## 项目目标

- 掌握 Prompt Engineering 基础方法
- 封装统一 LLM API 调用层
- 实现结构化输出、流式输出和工具调用原型
- 基于 FastAPI 构建可运行的 AI Assistant API
- 为 Nexus Research、Nexus Dev、Nexus Agent 三个项目提供公共能力

## 目录结构

```text
apps/       应用入口，例如 FastAPI 服务
packages/   可复用代码模块，例如模型客户端、工具函数
prompts/    Prompt 模板库
docs/       学习笔记、开发日志、截图记录
```

## 文档结构

```text
docs/
├── plans/    实习计划、周计划、路线图等规划类文档
├── logs/     每日开发日志
├── notes/    学习笔记
├── images/   环境截图、接口截图、运行截图
└── demos/    Demo 说明、录屏链接、展示素材
```

## 环境准备

### 使用 uv

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

## 当前进度

- [x] D1：项目定位与环境搭建
- [ ] D2：Prompt 基础
- [ ] D3：结构化输出
- [ ] D4：LLM API 调用封装
- [ ] D5：Function Calling
- [ ] D6：FastAPI AI 服务
- [ ] D7：复盘与包装