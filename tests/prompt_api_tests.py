"""
D2 Prompt API Tests

用途：
- 使用 ModelClient 通过 API 测试 D2 中尚未测试的 Dev Prompt 3 个、Agent Prompt 3 个。
- 将测试结果自动写入 docs/notes/prompt-api-test-results.md。

运行：
python tests/prompt_api_tests.py
"""

from pathlib import Path
from datetime import datetime

from packages.model_client import ModelClient


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT_DIR / "docs" / "notes" / "prompt-api-test-results.md"


DEV_TEST_INPUT_CODE = """def normalize_scores(scores):
    max_score = max(scores)
    return [score / max_score for score in scores]
"""

AGENT_TEST_INPUT_TASK = "我想做一个 AI 学习助手，可以根据我的学习目标生成每日计划，记录学习进度，并在每周末生成复盘报告。"


DEV_PROMPTS = [
    {
        "name": "Dev Prompt 1：基础代码解释",
        "model_type": "flash",
        "prompt": f"""你是一个资深软件工程师，擅长用清晰、结构化的方式解释代码。

你的任务是解释用户提供的代码，帮助读者快速理解这段代码的功能、执行流程和关键实现。

请阅读以下代码：

```python
{DEV_TEST_INPUT_CODE}
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
""",
    },
    {
        "name": "Dev Prompt 2：结构化代码分析",
        "model_type": "flash",
        "prompt": f"""你是一个代码分析助手，擅长将代码片段转化为结构化研发信息。

请分析以下代码：

```python
{DEV_TEST_INPUT_CODE}
```

请只基于代码本身进行分析。如果缺少上下文，请在 uncertainties 中说明，不要编造外部信息。

请只输出原始 JSON 对象，不要使用 Markdown 代码块，不要添加解释文字。

请按照以下 JSON 格式输出：

{{
  "summary": "一句话概括代码功能",
  "purpose": "这段代码的主要用途",
  "inputs": [
    {{
      "name": "输入名称",
      "type": "输入类型或推测类型",
      "description": "输入含义"
    }}
  ],
  "outputs": [
    {{
      "type": "输出类型或推测类型",
      "description": "输出含义"
    }}
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
}}
""",
    },
    {
        "name": "Dev Prompt 3：Few-shot 代码解释",
        "model_type": "flash",
        "prompt": f"""你是一个资深软件工程师。请参考示例的解释风格，对用户提供的代码进行说明。

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

```python
{DEV_TEST_INPUT_CODE}
```

请按照示例格式输出。
""",
    },
]


AGENT_PROMPTS = [
    {
        "name": "Agent Prompt 1：基础任务拆解",
        "model_type": "pro",
        "prompt": f"""你是一个任务规划助手，擅长将复杂目标拆解为清晰、可执行的步骤。

你的任务是根据用户提供的目标，生成一份任务拆解方案。

用户目标：

\"\"\"
{AGENT_TEST_INPUT_TASK}
\"\"\"

请遵守以下要求：
1. 不要只给泛泛建议，要拆成具体可执行步骤。
2. 每个步骤都要有明确目标和产出物。
3. 如果任务信息不足，请列出需要补充的问题。
4. 输出要适合后续交给 AI Agent 或人工执行。

请按照以下格式输出：

## 任务目标

## 任务拆解

### 阶段一：
- 目标：
- 具体步骤：
  1.
  2.
  3.
- 产出物：

### 阶段二：
- 目标：
- 具体步骤：
  1.
  2.
  3.
- 产出物：

### 阶段三：
- 目标：
- 具体步骤：
  1.
  2.
  3.
- 产出物：

## 需要补充的信息
-

## 最小可行版本
-
""",
    },
    {
        "name": "Agent Prompt 2：带优先级与依赖关系的任务拆解",
        "model_type": "pro",
        "prompt": f"""你是一个 AI 项目任务编排助手。

请将用户提供的复杂目标拆解为可执行任务，并标注优先级、依赖关系、建议执行角色和验收标准。

用户目标：

\"\"\"
{AGENT_TEST_INPUT_TASK}
\"\"\"

请遵守以下要求：
1. 任务必须具体、可执行、可验收。
2. 优先级只能使用 P0、P1、P2。
   - P0：必须先完成的核心任务
   - P1：重要但可在 P0 后完成的任务
   - P2：优化类或增强类任务
3. dependencies 中只能填写其他任务的 task_id。
4. 如果信息不足，请在 open_questions 中列出。
5. 不要编造用户没有提供的业务背景。
6. 请只输出原始 JSON 对象，不要使用 Markdown 代码块，不要添加解释文字。

请按照以下 JSON 格式输出：

{{
  "goal": "任务目标",
  "tasks": [
    {{
      "task_id": "T1",
      "title": "任务标题",
      "description": "任务描述",
      "priority": "P0",
      "dependencies": [],
      "suggested_role": "执行角色，例如 researcher/developer/tester/planner",
      "deliverable": "交付物",
      "acceptance_criteria": [
        "验收标准1",
        "验收标准2"
      ]
    }}
  ],
  "execution_order": ["T1", "T2", "T3"],
  "open_questions": [
    "需要用户补充的问题"
  ],
  "mvp_scope": [
    "最小可行版本范围"
  ]
}}
""",
    },
    {
        "name": "Agent Prompt 3：Few-shot 任务拆解",
        "model_type": "pro",
        "prompt": f"""你是一个任务拆解专家。请参考示例的拆解风格，将用户目标拆解为可执行计划。

示例 1：

用户目标：
我要做一个个人博客网站。

输出：

## 任务目标
构建一个可以展示文章、个人信息和项目作品的个人博客网站。

## 执行计划

### 阶段一：明确需求
- 确定博客目标用户
- 确定核心页面：主页、文章列表、文章详情、关于我、项目展示
- 明确是否需要后台管理功能

交付物：
- 页面清单
- 功能清单

### 阶段二：搭建基础项目
- 选择技术栈
- 初始化项目结构
- 配置路由和基础样式

交付物：
- 可运行的前端项目

### 阶段三：实现核心功能
- 实现文章列表
- 实现文章详情页
- 实现个人信息展示
- 实现项目展示区

交付物：
- 可浏览的博客原型

### 阶段四：优化与发布
- 优化页面样式
- 检查移动端适配
- 部署到线上平台

交付物：
- 可访问的线上博客

## 最小可行版本
- 主页
- 文章列表
- 文章详情页
- 基础部署

现在请拆解以下用户目标：

\"\"\"
{AGENT_TEST_INPUT_TASK}
\"\"\"

请按照示例格式输出。
""",
    },
]


def append_result(name: str, model_type: str, prompt: str, output: str) -> None:
    with OUTPUT_FILE.open("a", encoding="utf-8") as file:
        file.write(f"\n## {name}\n\n")
        file.write(f"- 测试时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"- 使用模型类型：`{model_type}`\n\n")
        file.write("### 测试输入\n\n")
        file.write("````text\n")
        file.write(prompt)
        file.write("\n````\n\n")
        file.write("### 测试输出\n\n")
        file.write("````text\n")
        file.write(output)
        file.write("\n````\n\n")
        file.write("### 输出观察\n\n")
        file.write("- 结构是否稳定：待人工确认\n")
        file.write("- 是否遵守约束：待人工确认\n")
        file.write("- 是否存在编造：待人工确认\n")
        file.write("- 是否适合复用：待人工确认\n\n")
        file.write("---\n")


def main() -> None:
    client = ModelClient()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        "# Prompt API 测试结果\n\n"
        "本文件记录 D2 中 Dev Prompt 与 Agent Prompt 的 API 测试结果。\n\n"
        "## 测试清单\n\n"
        "- [x] Dev Prompt 1：基础代码解释\n"
        "- [x] Dev Prompt 2：结构化代码分析\n"
        "- [x] Dev Prompt 3：Few-shot 代码解释\n"
        "- [x] Agent Prompt 1：基础任务拆解\n"
        "- [x] Agent Prompt 2：带优先级与依赖关系的任务拆解\n"
        "- [x] Agent Prompt 3：Few-shot 任务拆解\n",
        encoding="utf-8",
    )

    for item in DEV_PROMPTS + AGENT_PROMPTS:
        print(f"Running: {item['name']} ({item['model_type']})")
        output = client.chat(
            user_message=item["prompt"],
            system_message="你是一个严谨的 AI 应用开发助手，必须严格遵守用户给出的输出格式和约束。",
            temperature=0.2,
            model_type=item["model_type"],
        )
        append_result(item["name"], item["model_type"], item["prompt"], output)

    print(f"\nDone. Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
