# Day 04 开发日志：LLM API 调用与 ModelClient 封装

## 今日目标

- 理解 LLM API 调用流程
- 理解 system message、user message、temperature、streaming
- 封装统一模型调用入口 `ModelClient`
- 支持 default / flash / pro 模型选择
- 实现普通输出与流式输出
- 为 D5 Function Calling 和 D6 FastAPI Demo 打基础

## 今日完成

- [x] 创建 `packages/model_client.py`
- [x] 创建 LLM API 学习笔记
- [x] 实现 `.env` 配置读取
- [x] 实现 `ModelClient.__init__`
- [x] 实现 `_select_model()` 模型选择方法
- [x] 实现 `chat()` 普通文本调用
- [x] 实现 `stream_chat()` 流式文本调用
- [x] 支持 `default` / `flash` / `pro` 三类模型选择
- [x] 使用 DeepSeek API 完成普通调用测试
- [x] 使用 DeepSeek API 完成流式调用测试
- [x] 解决 VS Code 解释器选择问题
- [x] 解决 API Key 非 ASCII 字符导致的请求头编码问题
- [x] 解决 Responses API 与 DeepSeek 兼容性问题，改为 Chat Completions 兼容版
- [x] 使用 ModelClient 完成 Dev Prompt 3 个 API 测试
- [x] 使用 ModelClient 完成 Agent Prompt 3 个 API 测试
- [x] 使用 ModelClient 完成结构化输出 API 测试
- [x] 使用 Pydantic 校验 LLM 结构化输出

## 当前 .env 配置

```env
OPENAI_API_KEY=your_api_key
BASE_URL=https://api.deepseek.com

DEFAULT_MODEL=deepseek-v4-flash
FLASH_MODEL=deepseek-v4-flash
PRO_MODEL=deepseek-v4-pro
```

## 测试记录

### Default Model Test

测试任务：

```text
用三句话解释什么是 Prompt Engineering。
```

测试结果：

模型能够正常返回完整文本，说明默认模型调用成功。

### Flash Model Test

测试任务：

```text
用三句话解释什么是结构化输出。
```

测试结果：

模型能够使用 `flash` 模型完成简短解释，适合轻量级任务。

### Pro Model Test

测试任务：

```text
请从技术、产品、工程化三个角度分析 LLM API 封装在 AI 应用开发中的价值。
```

测试结果：

模型能够输出较完整的多维度分析，适合复杂分析任务。

### Streaming Flash Model Test

测试任务：

```text
用三句话解释什么是流式输出。
```

测试结果：

模型能够边生成边输出文本片段，说明流式调用成功。

## D2 / D3 遗留任务闭环

### D2 Prompt API 测试

测试命令：

```powershell
python -m tests.prompt_api_tests
```

测试结果：

```text
docs/notes/prompt-api-test-results.md
```

完成内容：

- Dev Prompt 3 个 API 测试
- Agent Prompt 3 个 API 测试
- D3 Structured Output API 测试

### D3 Structured Output API 测试

测试命令：

```powershell
python -m tests.structured_output_api_test
```

测试结果：

```text
docs/notes/structured-output-api-test-results.md
```

完成内容：

- summary API 输出测试
- classify API 输出测试
- extract API 输出测试
- Pydantic 校验测试

## 今日遇到的问题

### 问题 1：Responses API 404

现象：

```text
openai.NotFoundError: Error code: 404
```

原因：

DeepSeek 当前兼容的是 Chat Completions 风格接口，不支持 OpenAI Responses API。

解决：

将调用方式从：

```python
client.responses.create(...)
```

改为：

```python
client.chat.completions.create(...)
```

### 问题 2：VS Code 插件运行找不到 pydantic

现象：

```text
ModuleNotFoundError: No module named 'pydantic'
```

原因：

VS Code 选择了 uv 管理的基础 Python 解释器，而不是项目 `.venv` 解释器。

解决：

将 VS Code Python Interpreter 设置为：

```text
E:\Projects\Nexus\.venv\Scripts\python.exe
```

### 问题 3：API Key 出现 UnicodeEncodeError

现象：

```text
UnicodeEncodeError: 'ascii' codec can't encode characters
```

原因：

`.env` 中 API Key 曾出现中文占位符或非 ASCII 字符，请求头无法编码。

解决：

使用真实 API Key，并在 `ModelClient` 中对环境变量进行 `.strip()` 清理和非 ASCII 检查。

## 今日理解

D4 的核心不是单纯调用一次模型，而是将模型调用抽象为可复用的公共能力层。通过 `ModelClient`，后续可以让 Nexus Research、Nexus Dev、Nexus Agent 共用同一套模型访问逻辑。

## 遗留任务

- [ ] 增加 JSON 解析和 Pydantic 校验
- [ ] 增加统一异常处理
- [ ] 增加 Tool Calling 支持

## 明日计划

D5 将学习 Function Calling / Tool Calling，理解“模型负责决策，工具负责执行”的基本思想，并实现 2 个工具调用示例。

## D4 最终结论

D4 已完成 ModelClient 封装，并通过 DeepSeek API 验证普通调用、流式调用、flash / pro 模型切换能力。同时补充完成 D2 Prompt API 测试和 D3 结构化输出 API 测试，为 D5 Tool Calling 和 D6 FastAPI 服务封装打下基础。