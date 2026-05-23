# Structured Output API 测试结果

- 测试时间：2026-05-23 21:29:47
- 使用模型类型：`flash`

## Summary API Test

### Prompt

```text
请对以下文本进行结构化总结。

文本：
"""
5月22日，有“大模型第一股”之称的智谱（02513.HK）股价大涨，盘中一度涨超32%。
消息面上，智谱发布了GLM-5.1高速版。5月22日，智谱宣布，面向部分企业客户提供GLM-5.1高速版API“GLM-5.1-HighSpeed”，其模型输出速度达到400 Tokens/s，刷新当前全球大模型厂商API的速度上限。GLM-5.1高速版适用于AI编程、实时交互、商业决策、实时语音等对响应延迟要求极高的场景，现已面向智谱MaaS平台部分企业客户开放。
受此提振，港股人工智能应用股走强，另一大模型明星股MiniMax盘中一度涨超20%。
"""

请只输出原始 JSON 对象，不要使用 Markdown 代码块，不要添加解释文字。

JSON 格式如下：
{
  "summary": "一句话总结",
  "key_points": ["关键信息1", "关键信息2", "关键信息3"],
  "entities": ["实体1", "实体2"],
  "uncertainties": ["原文未提及或无法确认的信息"]
}

```

### Raw Output

```text
{
  "summary": "5月22日，智谱因发布GLM-5.1高速版API（输出速度400 Tokens/s）而股价大涨超32%，并带动港股AI应用股走强，MiniMax涨超20%。",
  "key_points": [
    "5月22日智谱股价盘中涨超32%。",
    "智谱发布GLM-5.1高速版API，输出速度400 Tokens/s，刷新全球大模型厂商API速度上限。",
    "该API面向部分企业客户开放，适用于AI编程、实时交互、商业决策等低延迟场景。",
    "受此提振，港股人工智能应用股走强，MiniMax盘中涨超20%。"
  ],
  "entities": [
    "智谱（02513.HK）",
    "GLM-5.1高速版",
    "MiniMax",
    "港股人工智能应用股"
  ],
  "uncertainties": [
    "未提及智谱股价后续走势。",
    "未提及GLM-5.1高速版的定价或全面开放时间。",
    "未提及MiniMax涨幅的具体原因是否完全归因于智谱。"
  ]
}
```

### Parsed Data

```json
{
  "summary": "5月22日，智谱因发布GLM-5.1高速版API（输出速度400 Tokens/s）而股价大涨超32%，并带动港股AI应用股走强，MiniMax涨超20%。",
  "key_points": [
    "5月22日智谱股价盘中涨超32%。",
    "智谱发布GLM-5.1高速版API，输出速度400 Tokens/s，刷新全球大模型厂商API速度上限。",
    "该API面向部分企业客户开放，适用于AI编程、实时交互、商业决策等低延迟场景。",
    "受此提振，港股人工智能应用股走强，MiniMax盘中涨超20%。"
  ],
  "entities": [
    "智谱（02513.HK）",
    "GLM-5.1高速版",
    "MiniMax",
    "港股人工智能应用股"
  ],
  "uncertainties": [
    "未提及智谱股价后续走势。",
    "未提及GLM-5.1高速版的定价或全面开放时间。",
    "未提及MiniMax涨幅的具体原因是否完全归因于智谱。"
  ]
}
```

### Pydantic Validation Result

校验成功。

```text
summary='5月22日，智谱因发布GLM-5.1高速版API（输出速度400 Tokens/s）而股价大涨超32%，并带动港股AI应用股走强，MiniMax涨超20%。' key_points=['5月22日智谱股价盘中涨超32%。', '智谱发布GLM-5.1高速版API，输出速度400 Tokens/s，刷新全球大模型厂商API速度上限。', '该API面向部分企业客户开放，适用于AI编程、实时交互、商业决策等低延迟场景。', '受此提振，港股人工智能应用股走强，MiniMax盘中涨超20%。'] entities=['智谱（02513.HK）', 'GLM-5.1高速版', 'MiniMax', '港股人工智能应用股'] uncertainties=['未提及智谱股价后续走势。', '未提及GLM-5.1高速版的定价或全面开放时间。', '未提及MiniMax涨幅的具体原因是否完全归因于智谱。']
```

---

## Classify API Test

### Prompt

```text
请对以下文本进行行业信息分类。

文本：
"""
5月22日，有“大模型第一股”之称的智谱（02513.HK）股价大涨，盘中一度涨超32%。
消息面上，智谱发布了GLM-5.1高速版。5月22日，智谱宣布，面向部分企业客户提供GLM-5.1高速版API“GLM-5.1-HighSpeed”，其模型输出速度达到400 Tokens/s，刷新当前全球大模型厂商API的速度上限。GLM-5.1高速版适用于AI编程、实时交互、商业决策、实时语音等对响应延迟要求极高的场景，现已面向智谱MaaS平台部分企业客户开放。
受此提振，港股人工智能应用股走强，另一大模型明星股MiniMax盘中一度涨超20%。
"""

分类标签只能从以下选项中选择：
- 技术突破
- 产品发布
- 融资并购
- 政策监管
- 市场竞争
- 商业合作
- 其他

请只输出原始 JSON 对象，不要使用 Markdown 代码块，不要添加解释文字。

JSON 格式如下：
{
  "category": "分类标签",
  "confidence": 0.0,
  "reason": "分类理由"
}

```

### Raw Output

```text
{
  "category": "产品发布",
  "confidence": 0.95,
  "reason": "文本主要描述智谱发布GLM-5.1高速版API，属于新产品的推出，因此归类为产品发布。"
}
```

### Parsed Data

```json
{
  "category": "产品发布",
  "confidence": 0.95,
  "reason": "文本主要描述智谱发布GLM-5.1高速版API，属于新产品的推出，因此归类为产品发布。"
}
```

### Pydantic Validation Result

校验成功。

```text
category='产品发布' confidence=0.95 reason='文本主要描述智谱发布GLM-5.1高速版API，属于新产品的推出，因此归类为产品发布。'
```

---

## Extract API Test

### Prompt

```text
请从以下文本中抽取结构化实体和关键信息。

文本：
"""
5月22日，有“大模型第一股”之称的智谱（02513.HK）股价大涨，盘中一度涨超32%。
消息面上，智谱发布了GLM-5.1高速版。5月22日，智谱宣布，面向部分企业客户提供GLM-5.1高速版API“GLM-5.1-HighSpeed”，其模型输出速度达到400 Tokens/s，刷新当前全球大模型厂商API的速度上限。GLM-5.1高速版适用于AI编程、实时交互、商业决策、实时语音等对响应延迟要求极高的场景，现已面向智谱MaaS平台部分企业客户开放。
受此提振，港股人工智能应用股走强，另一大模型明星股MiniMax盘中一度涨超20%。
"""

请只输出原始 JSON 对象，不要使用 Markdown 代码块，不要添加解释文字。

JSON 格式如下：
{
  "companies": ["公司或机构"],
  "products": ["产品名称"],
  "technologies": ["技术关键词"],
  "metrics": ["关键指标，如速度、金额、比例等"],
  "dates": ["日期信息"]
}

```

### Raw Output

```text
{
  "companies": ["智谱", "MiniMax"],
  "products": ["GLM-5.1高速版", "GLM-5.1-HighSpeed API", "MaaS平台"],
  "technologies": ["GLM-5.1高速版", "大模型", "AI编程", "实时交互", "商业决策", "实时语音"],
  "metrics": ["32%", "400 Tokens/s"],
  "dates": ["5月22日"]
}
```

### Parsed Data

```json
{
  "companies": [
    "智谱",
    "MiniMax"
  ],
  "products": [
    "GLM-5.1高速版",
    "GLM-5.1-HighSpeed API",
    "MaaS平台"
  ],
  "technologies": [
    "GLM-5.1高速版",
    "大模型",
    "AI编程",
    "实时交互",
    "商业决策",
    "实时语音"
  ],
  "metrics": [
    "32%",
    "400 Tokens/s"
  ],
  "dates": [
    "5月22日"
  ]
}
```

### Pydantic Validation Result

校验成功。

```text
companies=['智谱', 'MiniMax'] products=['GLM-5.1高速版', 'GLM-5.1-HighSpeed API', 'MaaS平台'] technologies=['GLM-5.1高速版', '大模型', 'AI编程', '实时交互', '商业决策', '实时语音'] metrics=['32%', '400 Tokens/s'] dates=['5月22日']
```

---

