# Structured Output with Pydantic

## 1. 什么是结构化输出

结构化输出是指让大模型按照固定字段、固定类型、固定格式返回内容，例如 JSON 对象。

相比自然语言输出，结构化输出更适合：

- 程序解析
- 数据库存储
- 前端展示
- 工作流编排
- 后续 API 调用

## 2. JSON、JSON Schema 和 Pydantic 的关系

- JSON：实际的数据格式
- JSON Schema：描述 JSON 应该长什么样的规则
- Pydantic：Python 中用于定义、校验和转换数据结构的工具

## 3. 为什么需要结构化输出

如果模型只输出自然语言，程序很难稳定处理。

例如：

```text
这条新闻主要讲智谱发布高速版 API。
```

程序不容易知道公司是谁、产品是什么、分类是什么。

如果输出 JSON：

```json
{
  "summary": "智谱发布高速版 API",
  "company": "智谱",
  "product": "GLM-5.1-HighSpeed",
  "category": "产品发布"
}
```

程序就可以直接读取字段。


## 4. Pydantic 的作用

Pydantic 可以帮助我们：

- 定义字段
- 限制字段类型
- 限制枚举值
- 设置默认值
- 校验错误数据
- 生成 JSON Schema

## 5. D3 实现内容

本日实现了三类结构化输出模型：

- `SummaryResult`：用于行业信息总结
- `ClassifyResult`：用于行业信息分类
- `ExtractResult`：用于实体和关键信息抽取

## 6. 今日理解

结构化输出的关键不是“让模型看起来像 JSON”，而是让输出能够被程序稳定解析、校验和复用。

## 7. 本地测试结论

本地测试分为两类：

### 正常数据测试

`summary_data`、`classify_data`、`extract_data` 均能被 Pydantic 正常解析，说明字段结构设计可用。

### 异常数据测试

测试了以下异常情况：

- `category` 不在允许分类集合中
- `confidence` 超出 0-1 范围
- 必填字段 `key_points` 缺失

Pydantic 能够准确捕获这些错误，说明程序端校验可以作为 Prompt 输出不稳定时的兜底机制。

## 8. D3 关键理解

Prompt 可以约束模型输出格式，但不能完全保证输出稳定。结构化输出需要同时依赖：

- Prompt 约束
- JSON 格式
- Pydantic 字段定义
- 程序端异常处理

这套机制会在 D4 的 `ModelClient` 中继续复用。
