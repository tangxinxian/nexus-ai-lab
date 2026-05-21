# Day 01 开发日志：定位与环境搭建

## 今日目标

- 明确 AI 应用开发工程师能力模型
- 配置 Python、虚拟环境、API Key
- 初始化 Nexus 项目仓库
- 创建基础目录结构和 README

## 今日完成

- [x] 创建项目目录
- [x] 使用 uv 固定 Python 3.11
- [x] 创建 Python 虚拟环境
- [x] 安装 openai、python-dotenv、fastapi、uvicorn、pydantic
- [x] 验证 Python 环境
- [x] 创建 apps / packages / prompts / docs 目录
- [x] 配置 .env
- [x] 配置 .gitignore
- [x] 编写 README 初版
- [ ] 初始化 Git 仓库并提交

## 今日理解

AI 应用开发工程师的核心能力不是训练大模型，而是将大模型能力集成到真实应用中，并通过 Prompt、API、工具调用和后端服务封装，构建可复用、可展示的 AI 应用能力。

本周的 Nexus Base Assistant 是后续 Nexus Research、Nexus Dev、Nexus Agent 三个项目的公共技术底座。

## 遇到的问题

### 问题 1：系统全局 python 命令不可用

现象：

```powershell
Python was not found; run without arguments to install from the Microsoft Store