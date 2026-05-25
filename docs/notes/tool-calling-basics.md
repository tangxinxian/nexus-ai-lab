# Tool Calling Basics

## 1. 什么是 Tool Calling

Tool Calling 是让大模型根据用户请求选择合适工具，并生成工具调用参数，再由程序执行工具的机制。

它的核心思想是：

```text
模型负责决策
工具负责执行
程序负责调度
```

在 D5 中，我们使用 DeepSeek 官方兼容 OpenAI Chat Completions 的 Tool Calls 流程完成了一个最小闭环。

## 2. Tool Calling 解决什么问题

普通 LLM 擅长语言理解和生成，但不擅长执行确定性操作，例如：

- 查询数据库
- 调用外部 API
- 获取网页内容
- 执行计算
- 读取文件
- 生成结构化任务清单
- 调用业务系统

Tool Calling 可以让模型把这些任务交给外部工具完成。

## 3. Function Calling 与 Tool Calling 的关系

Function Calling 通常指模型生成函数名和参数，由开发者代码执行函数。

Tool Calling 是更宽泛的概念，工具可以是：

- 本地函数
- 外部 API
- 数据库查询
- 文件系统操作
- 搜索引擎
- MCP 工具

在当前项目中，D5 先实现本地函数工具：

- `summarize_webpage_placeholder`
- `generate_task_list`

## 4. DeepSeek Tool Calls 基本流程

D5 使用的是 DeepSeek 官方 Tool Calls 风格，整体流程如下：

```text
用户请求
↓
模型根据 tools 定义判断是否需要调用工具
↓
模型返回 tool_calls
↓
程序解析 tool_name 和 arguments
↓
程序执行本地工具函数
↓
程序将工具结果作为 role="tool" 消息追加回 messages
↓
再次调用模型
↓
模型基于工具结果生成最终回答
```

## 5. D5 实现内容

本日实现了以下文件：

```text
packages/tools.py
tests/tool_calling_demo.py
```

### packages/tools.py

该文件负责：

- 定义本地工具函数
- 定义工具输入输出 Pydantic 模型
- 定义 `TOOL_DEFINITIONS`
- 定义 `run_tool()`
- 定义 `tool_result_to_json()`

当前工具包括：

```text
summarize_webpage_placeholder
generate_task_list
```

### tests/tool_calling_demo.py

该文件负责：

- 向模型传入 `tools=TOOL_DEFINITIONS`
- 获取模型返回的 `message.tool_calls`
- 执行本地工具
- 将工具结果作为 `role="tool"` 消息传回模型
- 获取最终自然语言回答

## 6. 工具定义说明

`TOOL_DEFINITIONS` 会告诉模型：

- 工具名称是什么
- 工具适合解决什么问题
- 工具需要哪些参数
- 参数类型是什么
- 参数是否必填
- 参数有哪些可选值

例如 `generate_task_list` 的工具定义会告诉模型：

```text
该工具用于根据用户目标生成结构化任务清单。
参数包括：
- goal：用户目标
- task_type：任务类型，可选 learning / project / research / general
```

模型并不会执行这个工具，它只会返回类似：

```json
{
  "name": "generate_task_list",
  "arguments": {
    "goal": "做一个 AI 学习助手",
    "task_type": "project"
  }
}
```

真正执行工具的是 Python 程序。

## 7. 本次测试结果

测试命令：

```powershell
python -m tests.tool_calling_demo
```

测试请求：

```text
请帮我把“做一个 AI 学习助手”拆解成项目任务清单。
```

模型成功返回工具调用：

```text
tool_name: generate_task_list
arguments: {"goal": "做一个 AI 学习助手", "task_type": "project"}
```

程序随后执行本地工具，并得到结构化任务清单：

```text
T1：明确需求
T2：搭建原型
T3：测试与优化
```

最后，模型基于工具结果生成了面向用户的任务拆解建议。

## 8. 与 Nexus 三大项目的关系

### Nexus Research

Tool Calling 可以用于：

- 网页抓取
- 信息摘要
- 资料检索
- 报告生成
- 引用检查

### Nexus Dev

Tool Calling 可以用于：

- 读取代码文件
- 分析代码结构
- 生成测试用例
- 调用 GitHub API
- 执行静态分析

### Nexus Agent

Tool Calling 是 Agent 的基础能力，可用于：

- 任务拆解
- 工具调度
- 多步骤执行
- 多 Agent 协作
- MCP 工具生态接入

## 9. 当前实现的边界

当前版本仍然是 D5 学习阶段实现，存在以下边界：

- `summarize_webpage_placeholder` 只是占位工具，不会真实抓取网页。
- `generate_task_list` 是规则型工具，暂未接入复杂项目规划逻辑。
- 工具调用异常处理较简单。
- 尚未实现工具调用链路日志记录。
- 尚未接入 FastAPI 服务。

## 10. 后续扩展方向

后续可以继续增强：

- 将网页摘要占位工具替换为真实网页抓取工具
- 为工具参数增加更严格的 JSON Schema
- 引入 DeepSeek strict mode 或 OpenAI Structured Outputs
- 增加工具执行异常处理
- 增加工具调用日志
- 将 Tool Calling 接入 FastAPI `/plan` 或 `/summarize` 接口
- 后续探索 LangGraph / MCP 工具编排

## 11. 今日理解

Tool Calling 的关键不是让模型“自己执行工具”，而是让模型产生结构化工具调用意图，再由程序执行真实工具。

这比让模型直接回答更可靠，也更适合构建可控、可复用、可扩展的 AI 应用。