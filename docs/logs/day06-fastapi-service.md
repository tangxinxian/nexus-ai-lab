# Day 06 开发日志：FastAPI AI 服务封装

## 今日目标

- 学习 FastAPI 基础接口开发方式
- 理解 `FastAPI()`、路由、请求模型、响应模型
- 将 D4 的 `ModelClient` 封装为 API 能力
- 将 D5 的任务拆解工具封装为 API 能力
- 实现 `/health`、`/chat`、`/summarize`、`/plan` 四个接口
- 在浏览器中通过 `/docs` 完成接口测试

## 今日完成

- [x] 创建 `apps/main.py`
- [x] 创建 `apps/__init__.py`
- [x] 创建 FastAPI 应用实例
- [x] 实现 `/health` 健康检查接口
- [x] 实现 `/chat` 普通对话接口
- [x] 实现 `/summarize` 行业信息总结接口
- [x] 实现 `/plan` 任务拆解接口
- [x] 使用 Pydantic 定义请求体和响应体
- [x] 使用 `response_model` 约束接口响应结构
- [x] 使用 `HTTPException` 处理模型调用异常
- [x] 本地启动 FastAPI 服务
- [x] 在 `/docs` 页面完成四个接口测试
- [x] 四个接口测试结果均符合预期

## 新增文件

```text
apps/__init__.py
apps/main.py
docs/notes/fastapi-basics.md
docs/logs/day06-fastapi-service.md
```

## 启动命令

```powershell
uvicorn apps.main:app --reload
```

启动成功后访问：

```text
http://127.0.0.1:8000/docs
```

健康检查接口：

```text
http://127.0.0.1:8000/health
```

## 接口测试记录

### 1. GET /health

用途：

检查 FastAPI 服务是否正常运行。

预期返回：

```json
{
  "status": "ok",
  "service": "Nexus Base Assistant API",
  "version": "0.1.0"
}
```

测试结果：

- [x] 接口可访问
- [x] 返回结构符合预期
- [x] 不依赖模型 API，适合作为健康检查接口

### 2. POST /chat

用途：

普通 AI 对话接口，调用 D4 的 `ModelClient.chat()`。

测试请求：

```json
{
  "message": "用三句话解释什么是 FastAPI。",
  "model_type": "flash",
  "temperature": 0.3
}
```

测试结果：

- [x] 请求参数校验正常
- [x] 模型调用成功
- [x] 返回 `reply` 和 `model_type`
- [x] 接口表现符合预期

### 3. POST /summarize

用途：

行业信息总结接口，接收行业文本并调用模型生成结构化总结。

测试请求：

```json
{
  "text": "智谱发布 GLM-5.1 高速版 API，模型输出速度达到 400 Tokens/s，适用于 AI 编程、实时交互、商业决策和实时语音等低延迟场景。",
  "model_type": "flash"
}
```

测试结果：

- [x] 请求参数校验正常
- [x] 模型调用成功
- [x] 输出包含行业信息总结
- [x] 接口表现符合预期

### 4. POST /plan

用途：

任务拆解接口，调用 D5 的 `generate_task_list()` 本地工具。

测试请求：

```json
{
  "goal": "做一个 AI 学习助手",
  "task_type": "project"
}
```

测试结果：

- [x] 请求参数校验正常
- [x] 本地工具调用成功
- [x] 返回结构化任务清单
- [x] 接口表现符合预期

## 今日理解

D6 的核心是将前几天完成的脚本能力封装为可通过 HTTP 调用的 AI API 服务。

当前实现中：

- `/chat` 复用了 D4 的 `ModelClient`
- `/summarize` 复用了 D2 的 Research Prompt 思想和 D4 的 `ModelClient`
- `/plan` 复用了 D5 的任务拆解工具
- FastAPI 通过 Pydantic 自动完成请求体校验、响应体约束和接口文档生成

这标志着 Nexus AI Lab 已从“本地脚本项目”升级为“最小可运行 AI 服务原型”。

## 与前几天内容的关系

### 与 D2 Prompt 的关系

`/summarize` 使用了 D2 中行业信息总结 Prompt 的思想，用于生成结构化行业摘要。

后续可以进一步将 Prompt 从 `apps/main.py` 中抽离，改为从 `prompts/research/industry-summary.md` 加载。

### 与 D3 结构化输出的关系

D6 当前使用 Pydantic 定义 API 请求和响应结构。

后续可以将 D3 的 `SummaryResult`、`ClassifyResult`、`ExtractResult` 接入 `/summarize`，让总结结果从 Markdown 字符串升级为严格结构化 JSON。

### 与 D4 ModelClient 的关系

`/chat` 和 `/summarize` 都通过 `ModelClient` 调用模型。

这说明 D4 的模型调用封装已经可以作为服务层能力复用。

### 与 D5 Tool Calling 的关系

`/plan` 直接调用 D5 的 `generate_task_list()` 工具函数。

D5 中验证的是模型通过 Tool Calls 选择工具；D6 中实现的是明确业务接口直接调用工具，保证服务稳定性。

## 今日收获

- 理解了 FastAPI 的基本开发方式
- 理解了请求模型和响应模型的作用
- 理解了 `response_model` 对接口文档和响应结构的价值
- 理解了如何将 AI 能力封装成 HTTP API
- 完成了 Nexus Base Assistant 的最小 API 服务原型

## 当前实现的边界

- `/summarize` 暂时返回 Markdown 字符串，尚未接入严格结构化输出。
- `/plan` 暂时直接调用本地工具，尚未通过 Tool Calls 自动决策。
- 当前接口为同步实现，后续可考虑异步化。
- 暂未增加接口自动化测试。
- 暂未增加日志记录和调用耗时统计。
- 暂未加入权限控制或 API Key 鉴权。

## 遗留任务

- [ ] 将 Prompt 模板从 `prompts/` 目录中加载
- [ ] 将 D3 结构化输出模型接入 `/summarize`
- [ ] 将 Tool Calling 能力接入 `/plan` 或新增 Agent 接口
- [ ] 增加 FastAPI 接口测试脚本
- [ ] 增加运行截图，用于 D7 项目包装
- [ ] 更新 README 中 D6 进度和运行方式

## 明日计划

D7 将进入 W1 复盘与项目包装，重点完成：

- README 最终整理
- W1 周总结
- Demo 截图或录屏
- GitHub 项目展示检查
- W2 学习计划准备
- 将 Nexus Base Assistant 包装成可展示的项目成果