# FastAPI Basics

## 1. 什么是 FastAPI

FastAPI 是一个用于构建 API 服务的 Python Web 框架，适合快速开发后端接口、AI 服务接口和数据处理服务。

在 Nexus AI Lab 中，FastAPI 的作用是把前面几天完成的能力封装成可被外部调用的 HTTP API：

- D2：Prompt 模板能力
- D3：结构化输出能力
- D4：ModelClient 模型调用能力
- D5：Tool Calling / 工具函数能力

D6 的目标是让这些能力从“脚本可运行”升级为“服务可调用”。

## 2. FastAPI 的核心概念

### app

`app = FastAPI()` 是整个 API 服务的入口。

```python
app = FastAPI(
    title="Nexus Base Assistant API",
    description="Nexus AI Lab W1 FastAPI Demo",
    version="0.1.0",
)
```

### 路由

路由用于定义接口路径和请求方法。

```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

```python
@app.post("/chat")
def chat(request: ChatRequest):
    ...
```

常见请求方法：

- `GET`：读取信息，例如健康检查
- `POST`：提交数据并触发处理，例如模型对话、文本总结、任务拆解

### Pydantic 请求模型

FastAPI 通常使用 Pydantic 定义请求体。

```python
class ChatRequest(BaseModel):
    message: str
    model_type: Literal["default", "flash", "pro"] = "flash"
    temperature: float = Field(default=0.3, ge=0, le=2)
```

这样可以自动完成：

- 请求字段校验
- 类型校验
- 默认值填充
- Swagger 文档生成

### Pydantic 响应模型

`response_model` 用于声明接口返回结构。

```python
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    ...
```

好处是：

- 响应结构清晰
- 自动生成 API 文档
- 避免返回多余字段
- 更适合前后端协作

## 3. D6 实现的 API

本日实现文件：

```text
apps/main.py
```

当前提供四个接口：

```text
GET  /health
POST /chat
POST /summarize
POST /plan
```

## 4. /health 接口

### 作用

用于检查 FastAPI 服务是否正常运行。

### 请求方式

```text
GET /health
```

### 返回示例

```json
{
  "status": "ok",
  "service": "Nexus Base Assistant API",
  "version": "0.1.0"
}
```

### 说明

该接口不调用模型，也不依赖外部 API，因此适合作为服务健康检查接口。

## 5. /chat 接口

### 作用

普通 AI 对话接口，接收用户输入并调用 `ModelClient.chat()` 返回模型回复。

### 请求方式

```text
POST /chat
```

### 请求示例

```json
{
  "message": "用三句话解释什么是 FastAPI。",
  "model_type": "flash",
  "temperature": 0.3
}
```

### 返回示例

```json
{
  "reply": "FastAPI 是一个现代 Python Web 框架...",
  "model_type": "flash"
}
```

### 对应能力

该接口复用了 D4 的 `ModelClient`：

```python
reply = model_client.chat(
    user_message=request.message,
    system_message="你是 Nexus Base Assistant，一个专业、清晰、可靠的 AI 应用开发助手。",
    temperature=request.temperature,
    model_type=request.model_type,
)
```

## 6. /summarize 接口

### 作用

行业信息总结接口，接收一段行业文本，调用模型生成结构化总结。

### 请求方式

```text
POST /summarize
```

### 请求示例

```json
{
  "text": "智谱发布 GLM-5.1 高速版 API，模型输出速度达到 400 Tokens/s，适用于 AI 编程、实时交互、商业决策和实时语音等低延迟场景。",
  "model_type": "flash"
}
```

### 返回示例

```json
{
  "summary": "## 一句话总结\n智谱发布 GLM-5.1 高速版 API...",
  "model_type": "flash"
}
```

### 对应能力

该接口复用了 D2 的 Research Prompt 思想，并通过 D4 的 `ModelClient` 调用模型。

当前版本中，Prompt 暂时写在 `apps/main.py` 中。后续可以优化为从 `prompts/research/industry-summary.md` 中读取模板。

## 7. /plan 接口

### 作用

任务拆解接口，接收用户目标和任务类型，返回结构化任务清单。

### 请求方式

```text
POST /plan
```

### 请求示例

```json
{
  "goal": "做一个 AI 学习助手",
  "task_type": "project"
}
```

### 返回示例

```json
{
  "goal": "做一个 AI 学习助手",
  "task_type": "project",
  "tasks": [
    {
      "task_id": "T1",
      "title": "明确需求",
      "description": "定义项目目标、核心用户、功能范围和验收标准。",
      "priority": "P0",
      "deliverable": "需求说明文档"
    }
  ]
}
```

### 对应能力

该接口直接复用了 D5 中的本地工具函数：

```python
result = generate_task_list(
    goal=request.goal,
    task_type=request.task_type,
)
```

当前 `/plan` 是明确业务接口，因此不需要让模型判断是否调用工具，而是直接调用对应工具函数，保证稳定性。

## 8. 运行方式

启动 FastAPI 服务：

```powershell
uvicorn apps.main:app --reload
```

启动成功后，终端会显示类似：

```text
Uvicorn running on http://127.0.0.1:8000
```

访问接口文档：

```text
http://127.0.0.1:8000/docs
```

访问健康检查：

```text
http://127.0.0.1:8000/health
```

## 9. Swagger UI

FastAPI 会自动生成 Swagger UI 文档页面。

在 `/docs` 页面中可以直接测试：

- `/health`
- `/chat`
- `/summarize`
- `/plan`

这使得 D6 Demo 非常适合截图和展示。

## 10. D6 关键理解

D6 的核心不是写一个复杂后端，而是完成从“脚本能力”到“服务能力”的升级。

整体调用链路如下：

```text
HTTP 请求
↓
FastAPI 接收请求
↓
Pydantic 校验请求体
↓
调用 ModelClient 或本地工具
↓
Pydantic 组织响应体
↓
返回 JSON 响应
```

这说明当前项目已经具备 AI 应用服务化的基本形态。

## 11. 当前实现的边界

当前版本是 W1 Demo 阶段实现，仍存在一些边界：

- `/summarize` 的 Prompt 暂时写在 `main.py` 中，尚未从 Prompt 模板库读取。
- `/plan` 当前直接调用本地工具，尚未接入 Tool Calls 自动决策。
- 接口是同步函数，后续可改为异步。
- 错误处理较基础，后续可增加统一异常处理模块。
- 尚未增加请求日志、模型调用日志和耗时统计。
- 尚未增加 API 自动化测试。

## 12. 后续优化方向

后续可以继续优化：

- 将 Prompt 模板从 `prompts/` 目录中加载
- 将结构化输出 Pydantic 模型接入 `/summarize`
- 将 Tool Calling 接入 `/plan` 或新增 `/agent/plan`
- 增加接口测试脚本
- 增加统一配置模块
- 增加日志与错误处理
- 增加前端页面或 Demo 录屏