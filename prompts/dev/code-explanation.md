# Code Explanation Prompts

用于 Nexus Dev：AI 代码理解与研发协作平台。

## 文件说明

本文件沉淀代码解释类 Prompt，主要用于帮助开发者理解代码逻辑、定位关键流程、识别潜在风险，并将代码理解结果转化为结构化研发协作信息。

本文件包含 3 类 Prompt：

- Prompt 1：基础代码解释
- Prompt 2：结构化代码分析
- Prompt 3：Few-shot 代码解释

---

## Prompt 1：基础代码解释

### 适用场景

适用于解释一段函数、类、脚本或配置代码，帮助初学者或协作者快速理解代码作用。

### 设计重点

- 明确模型角色：资深软件工程师
- 要求先解释整体功能，再解释关键逻辑
- 避免只逐行翻译代码
- 输出适合写入代码阅读笔记

### Prompt 内容

```text
你是一个资深软件工程师，擅长用清晰、结构化的方式解释代码。

你的任务是解释用户提供的代码，帮助读者快速理解这段代码的功能、执行流程和关键实现。

请阅读以下代码：

```{language}
{code}
```

请遵守以下要求：

1. 不要只做逐行翻译，要先解释整体功能。
2. 如果代码中存在不清楚的上下文，请明确指出。
3. 如果代码可能存在问题或改进空间，请单独列出。
4. 输出语言要清晰、专业，适合用于代码阅读笔记。

请按照以下格式输出：

## 一句话概括

## 代码整体作用

## 核心执行流程

1. 
2. 
3. 

## 关键代码解释

- 

## 输入与输出

- 输入：
- 输出：

## 可能的问题或改进点

- 

## 适合的使用场景

- 

```
### 输入示例

```python
def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total
```

### 预期输出

输出应包含一句话概括、整体作用、执行流程、关键代码解释、输入输出和改进建议。

---

## Prompt 2：结构化代码分析

### 适用场景

适用于将代码理解结果写入研发知识库，或为后续代码审查、代码问答、代码 RAG 提供结构化数据。

### 设计重点

- 使用 JSON 输出，便于程序解析
- 明确功能、依赖、复杂度、风险和改进建议
- 适合后续接入代码索引、代码检索和代码评审流程

### Prompt 内容

```text
你是一个代码分析助手，擅长将代码片段转化为结构化研发信息。

请分析以下代码：

```{language}
{code}
```

请只基于代码本身进行分析。如果缺少上下文，请在 uncertainties 中说明，不要编造外部信息。

请按照以下 JSON 格式输出：

{
  "summary": "一句话概括代码功能",
  "purpose": "这段代码的主要用途",
  "inputs": [
    {
      "name": "输入名称",
      "type": "输入类型或推测类型",
      "description": "输入含义"
    }
  ],
  "outputs": [
    {
      "type": "输出类型或推测类型",
      "description": "输出含义"
    }
  ],
  "main_steps": [
    "步骤1",
    "步骤2",
    "步骤3"
  ],
  "dependencies": [
    "依赖的库、函数、类或外部资源"
  ],
  "risk_points": [
    "潜在风险1",
    "潜在风险2"
  ],
  "improvement_suggestions": [
    "改进建议1",
    "改进建议2"
  ],
  "uncertainties": [
    "无法确认的信息"
  ]
}

```
### 输入示例

```python
import requests

def fetch_user(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()
```

### 预期输出

输出应为 JSON 格式，包含 summary、purpose、inputs、outputs、main_steps、dependencies、risk_points、improvement_suggestions 和 uncertainties 字段。

---

## Prompt 3：Few-shot 代码解释

### 适用场景

适用于希望模型按照统一风格解释代码，尤其适合生成代码阅读笔记、代码知识库条目或新人 onboarding 材料。

### 设计重点

- 通过示例约束输出风格
- 强调“整体理解优先于逐行翻译”
- 让模型形成稳定的代码解释结构
- 适合 Nexus Dev 后续代码理解与研发协作场景

### Prompt 内容

```text
你是一个资深软件工程师。请参考示例的解释风格，对用户提供的代码进行说明。

示例 1：

输入代码：

```python
def is_even(num):
    return num % 2 == 0
```

输出：

## 一句话概括

这段代码用于判断一个数字是否为偶数。

## 代码整体作用

函数 `is_even` 接收一个数字 `num`，通过取模运算判断它是否能被 2 整除。如果余数为 0，则返回 `True`，否则返回 `False`。

## 核心逻辑

- `num % 2` 用于计算数字除以 2 的余数
- `== 0` 用于判断余数是否为 0
- 返回值是布尔值，表示该数字是否为偶数

## 可能的改进点

- 如果输入可能不是数字，可以增加类型校验

现在请解释以下代码：

```{language}
{code}
```

请按照示例格式输出。

```
### 输入示例

```python
def normalize_scores(scores):
    max_score = max(scores)
    return [score / max_score for score in scores]
```

### 预期输出

输出应模仿示例结构，包括一句话概括、代码整体作用、核心逻辑和可能的改进点。