# LLM API Basics

## 1. LLM API 调用流程

LLM API 调用通常包括：

1. 准备 API Key
2. 配置模型名称和 API Base URL
3. 组织 system message 和 user message
4. 设置 temperature、stream 等参数
5. 发起请求
6. 解析响应
7. 处理异常

## 2. 为什么要封装 ModelClient

如果在每个业务文件中直接调用模型 API，会带来以下问题：

- API Key 管理分散
- 模型名称重复配置
- 普通调用、流式调用、结构化调用难以复用
- 错误处理逻辑分散
- 后续接入 FastAPI、Agent、RAG 时维护成本高

因此需要封装统一的 `ModelClient`，作为 Nexus 三大项目的公共模型访问层。

## 3. 当前 .env 配置

```env
OPENAI_API_KEY=your_api_key
BASE_URL=https://api.deepseek.com

DEFAULT_MODEL=deepseek-v4-flash
FLASH_MODEL=deepseek-v4-flash
PRO_MODEL=deepseek-v4-pro
```

说明：

- `DEFAULT_MODEL`：默认模型
- `FLASH_MODEL`：适合简单任务、快速任务、低成本任务
- `PRO_MODEL`：适合复杂分析、长文本理解、复杂推理任务

## 4. 模型选择策略

### Flash 模型适合

- 简短问答
- Prompt 测试
- 简单总结
- 信息分类
- 简单信息抽取
- 批量测试

### Pro 模型适合

- 深度行业分析
- 复杂代码理解
- 多步骤任务规划
- 长文本总结
- 复杂 Agent 推理
- 最终报告生成

## 5. 普通调用与流式调用

### 普通调用

普通调用会等待模型生成完整结果后一次性返回。

适合：

- 分类
- 摘要
- 信息抽取
- 结构化输出
- 后端接口调用

### 流式调用

流式调用会边生成边返回内容片段。

适合：

- 聊天界面
- 长文本生成
- 实时交互
- 提升用户等待体验

## 6. temperature 参数

`temperature` 用于控制模型输出的随机性。

- 较低 temperature：输出更稳定，适合分类、抽取、结构化输出
- 较高 temperature：输出更发散，适合创意写作、头脑风暴

当前默认使用：

```python
temperature=0.3
```

## 7. D4 实现内容

本日实现了 `packages/model_client.py`，包括：

- `ModelClient.__init__()`：读取 API Key、base_url 和模型配置
- `_select_model()`：根据 `default`、`flash`、`pro` 选择模型
- `chat()`：普通文本调用
- `stream_chat()`：流式文本调用

## 8. 本地测试结果

完成了四类测试：

- Default Model Test
- Flash Model Test
- Pro Model Test
- Streaming Flash Model Test

测试结果表明：

- `.env` 配置能够被正确读取
- DeepSeek API 调用成功
- `flash` 与 `pro` 模型可以通过 `model_type` 参数切换
- 普通调用与流式调用均可正常工作

## 9. D4 关键理解

`ModelClient` 不是简单的 API wrapper，而是后续 Nexus Research、Nexus Dev、Nexus Agent 的公共模型访问层。

通过统一封装模型调用，可以实现：

- 多模型适配
- API Key 安全管理
- 调用逻辑复用
- 后续结构化输出接入
- 后续 Tool Calling 接入
- 后续 FastAPI 服务封装