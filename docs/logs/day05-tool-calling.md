# Day 05 开发日志：Function Calling / Tool Calling

## 今日目标

- 理解 Function Calling / Tool Calling 的基本思想
- 理解“模型负责决策，工具负责执行，程序负责调度”
- 实现网页摘要占位工具
- 实现任务清单生成工具
- 基于 DeepSeek 官方 Tool Calls 流程完成一个工具调用 Demo

## 今日完成

- [x] 创建 `packages/tools.py`
- [x] 实现 `summarize_webpage_placeholder`
- [x] 实现 `generate_task_list`
- [x] 定义工具输入输出 Pydantic 模型
- [x] 定义 `TOOL_DEFINITIONS`
- [x] 实现 `run_tool()`
- [x] 实现 `tool_result_to_json()`
- [x] 创建 `tests/tool_calling_demo.py`
- [x] 使用 DeepSeek Tool Calls 完成“模型选择工具 → 程序执行工具 → 模型整理结果”的最小闭环
- [x] 完成 D5 工具调用测试

## 新增文件

```text
packages/tools.py
tests/tool_calling_demo.py
docs/notes/tool-calling-basics.md
docs/logs/day05-tool-calling.md
```

## 测试命令

### 本地工具测试

```powershell
python packages\tools.py
```

### Tool Calling Demo 测试

```powershell
python -m tests.tool_calling_demo
```

## 测试记录

### 用户请求

```text
请帮我把“做一个 AI 学习助手”拆解成项目任务清单。
```

### Step 1：模型判断是否调用工具

模型成功返回工具调用：

```text
tool_call_id: call_00_emXUmNObNAqkRCGwnOlg7632
tool_name: generate_task_list
arguments: {"goal": "做一个 AI 学习助手", "task_type": "project"}
```

说明模型根据用户请求和 `TOOL_DEFINITIONS` 判断该任务适合调用 `generate_task_list` 工具。

### Step 2：程序执行本地工具

程序执行：

```python
run_tool(
    tool_name="generate_task_list",
    arguments={
        "goal": "做一个 AI 学习助手",
        "task_type": "project"
    }
)
```

工具返回结构化任务清单：

```text
T1：明确需求
T2：搭建原型
T3：测试与优化
```

### Step 3：模型基于工具结果生成最终回答

程序将工具执行结果作为 `role="tool"` 消息追加回 `messages`，再次调用模型。

模型基于工具结果生成了更完整的项目任务拆解，包括：

- 明确需求
- 搭建原型
- 测试与优化
- 可选扩展
- 建议执行顺序

## 今日遇到的问题

### 问题 1：是否使用模拟 Tool Calling 还是官方 Tool Calls

最初可以通过“模型输出 JSON → 程序解析 JSON → 执行工具”的方式模拟工具调用流程。

但 DeepSeek 官方文档已经支持 Tool Calls，因此 D5 最终采用官方 Tool Calls 流程。

最终实现方式：

```python
client.chat.completions.create(
    model=model_client.pro_model,
    messages=messages,
    tools=TOOL_DEFINITIONS,
    tool_choice="auto",
)
```

### 问题 2：模型是否一定会调用工具

在 `tool_choice="auto"` 模式下，模型可以调用工具，也可以直接回答。

本次测试中，模型成功调用了 `generate_task_list`。

后续如果希望强制调用某个工具，可以将 `tool_choice` 改为指定函数调用。

## 今日理解

Tool Calling 是 Agent 能力的基础。

模型本身并不直接执行工具，而是根据用户请求和工具定义生成工具调用意图，包括工具名称和参数。真正执行工具的是程序，程序执行后再把工具结果返回给模型，由模型生成最终面向用户的回答。

这形成了一个清晰的执行闭环：

```text
用户请求
↓
模型选择工具
↓
程序执行工具
↓
工具结果返回模型
↓
模型生成最终回答
```

## 与前几天内容的关系

### 与 D2 Prompt 的关系

D2 的 Prompt 负责约束模型输出风格和任务边界。

D5 的 Tool Calling 则进一步让模型从“直接生成答案”升级为“选择工具并生成参数”。

### 与 D3 结构化输出的关系

工具参数和工具结果都需要结构化数据。

D3 中学习的 Pydantic 模型可以用于：

- 校验工具输入参数
- 校验工具输出结果
- 将工具结果转成标准 JSON

### 与 D4 ModelClient 的关系

D4 的 `ModelClient` 提供了模型访问能力。

D5 在此基础上直接使用：

```python
model_client.client.chat.completions.create(...)
```

完成工具调用测试。

## 遗留任务

- [ ] 将网页摘要占位工具替换为真实网页抓取工具
- [ ] 为 Tool Calling 增加更完善的异常处理
- [ ] 增加工具调用日志记录
- [ ] 将 Tool Calling 能力接入 D6 FastAPI 服务
- [ ] 后续探索 LangGraph / MCP 工具编排

## 明日计划

D6 将学习 FastAPI AI 服务封装，重点实现：

- `/chat` 接口
- `/summarize` 接口
- `/plan` 接口

并将以下能力初步接入 API 服务：

- `ModelClient`
- Prompt Library
- Structured Output
- Tool Calling