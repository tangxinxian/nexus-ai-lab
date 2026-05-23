"""
D3 Structured Output API Test

用途：
- 使用 ModelClient 调用 LLM API。
- 让模型返回 summary / classify / extract 三类 JSON。
- 使用 packages/structured_output.py 中的 Pydantic 模型进行校验。
- 将测试结果写入 docs/notes/structured-output-api-test-results.md。

运行：
python tests/structured_output_api_test.py
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Any

from packages.model_client import ModelClient
from packages.structured_output import (
    safe_parse_summary,
    safe_parse_classify,
    safe_parse_extract,
)


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT_DIR / "docs" / "notes" / "structured-output-api-test-results.md"

TEST_TEXT = """5月22日，有“大模型第一股”之称的智谱（02513.HK）股价大涨，盘中一度涨超32%。
消息面上，智谱发布了GLM-5.1高速版。5月22日，智谱宣布，面向部分企业客户提供GLM-5.1高速版API“GLM-5.1-HighSpeed”，其模型输出速度达到400 Tokens/s，刷新当前全球大模型厂商API的速度上限。GLM-5.1高速版适用于AI编程、实时交互、商业决策、实时语音等对响应延迟要求极高的场景，现已面向智谱MaaS平台部分企业客户开放。
受此提振，港股人工智能应用股走强，另一大模型明星股MiniMax盘中一度涨超20%。"""


def extract_json_object(text: str) -> dict[str, Any]:
    """从模型输出中提取 JSON 对象。

    理想情况下模型只输出原始 JSON。
    该函数用于兜底处理模型偶尔输出 ```json ... ``` 的情况。
    """
    content = text.strip()

    if content.startswith("```"):
        lines = content.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        content = "\n".join(lines).strip()

    start = content.find("{")
    end = content.rfind("}")

    if start == -1 or end == -1 or end <= start:
        raise ValueError("No valid JSON object found in model output.")

    return json.loads(content[start : end + 1])


def run_json_task(client: ModelClient, task_name: str, prompt: str) -> tuple[str, dict[str, Any]]:
    print(f"Running: {task_name}")
    raw_output = client.chat(
        user_message=prompt,
        system_message="你是一个严谨的信息抽取助手。请严格输出原始 JSON 对象，不要输出 Markdown 代码块或额外解释。",
        temperature=0.1,
        model_type="flash",
    )
    data = extract_json_object(raw_output)
    return raw_output, data


def main() -> None:
    client = ModelClient()

    summary_prompt = f"""请对以下文本进行结构化总结。

文本：
\"\"\"
{TEST_TEXT}
\"\"\"

请只输出原始 JSON 对象，不要使用 Markdown 代码块，不要添加解释文字。

JSON 格式如下：
{{
  "summary": "一句话总结",
  "key_points": ["关键信息1", "关键信息2", "关键信息3"],
  "entities": ["实体1", "实体2"],
  "uncertainties": ["原文未提及或无法确认的信息"]
}}
"""

    classify_prompt = f"""请对以下文本进行行业信息分类。

文本：
\"\"\"
{TEST_TEXT}
\"\"\"

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
{{
  "category": "分类标签",
  "confidence": 0.0,
  "reason": "分类理由"
}}
"""

    extract_prompt = f"""请从以下文本中抽取结构化实体和关键信息。

文本：
\"\"\"
{TEST_TEXT}
\"\"\"

请只输出原始 JSON 对象，不要使用 Markdown 代码块，不要添加解释文字。

JSON 格式如下：
{{
  "companies": ["公司或机构"],
  "products": ["产品名称"],
  "technologies": ["技术关键词"],
  "metrics": ["关键指标，如速度、金额、比例等"],
  "dates": ["日期信息"]
}}
"""

    tasks = [
        ("Summary API Test", summary_prompt, safe_parse_summary),
        ("Classify API Test", classify_prompt, safe_parse_classify),
        ("Extract API Test", extract_prompt, safe_parse_extract),
    ]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        file.write("# Structured Output API 测试结果\n\n")
        file.write(f"- 测试时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("- 使用模型类型：`flash`\n\n")

        for task_name, prompt, parser in tasks:
            raw_output, data = run_json_task(client, task_name, prompt)
            parsed = parser(data)

            file.write(f"## {task_name}\n\n")
            file.write("### Prompt\n\n")
            file.write("```text\n")
            file.write(prompt)
            file.write("\n```\n\n")
            file.write("### Raw Output\n\n")
            file.write("```text\n")
            file.write(raw_output)
            file.write("\n```\n\n")
            file.write("### Parsed Data\n\n")
            file.write("```json\n")
            file.write(json.dumps(data, ensure_ascii=False, indent=2))
            file.write("\n```\n\n")
            file.write("### Pydantic Validation Result\n\n")
            if parsed is None:
                file.write("校验失败。\n\n")
            else:
                file.write("校验成功。\n\n")
                file.write("```text\n")
                file.write(str(parsed))
                file.write("\n```\n\n")
            file.write("---\n\n")

    print(f"\nDone. Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
