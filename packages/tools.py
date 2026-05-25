import json
from typing import Any, Literal

from pydantic import BaseModel, Field


class WebpageSummaryInput(BaseModel):
    """网页摘要工具输入。"""

    url: str = Field(description="网页 URL")
    focus: str = Field(default="核心内容", description="摘要关注点")


class WebpageSummaryResult(BaseModel):
    """网页摘要工具输出。"""

    url: str
    focus: str
    summary: str
    key_points: list[str]
    limitations: list[str]


class TaskListInput(BaseModel):
    """任务清单生成工具输入。"""

    goal: str = Field(description="用户目标")
    task_type: Literal["learning", "project", "research", "general"] = Field(
        default="general",
        description="任务类型",
    )


class TaskItem(BaseModel):
    """单个任务项。"""

    task_id: str
    title: str
    description: str
    priority: Literal["P0", "P1", "P2"]
    deliverable: str


class TaskListResult(BaseModel):
    """任务清单生成工具输出。"""

    goal: str
    task_type: str
    tasks: list[TaskItem]


def summarize_webpage_placeholder(
    url: str,
    focus: str = "核心内容",
) -> WebpageSummaryResult:
    """网页摘要占位工具。

    当前版本不访问真实网页，只返回模拟摘要。
    D5 的重点是理解 Tool Calling 流程，不处理真实网页抓取。
    """

    return WebpageSummaryResult(
        url=url,
        focus=focus,
        summary=f"这是针对网页 {url} 的模拟摘要，摘要重点是：{focus}。",
        key_points=[
            "该工具当前为占位实现，不进行真实网页抓取。",
            "后续可接入 requests、BeautifulSoup、Playwright 或搜索 API。",
            "该工具用于演示模型调用外部工具的基本流程。",
        ],
        limitations=[
            "未访问真实网页内容。",
            "摘要内容为模拟结果。",
            "不能用于真实研究结论。",
        ],
    )


def generate_task_list(
    goal: str,
    task_type: Literal["learning", "project", "research", "general"] = "general",
) -> TaskListResult:
    """任务清单生成工具。

    根据用户目标和任务类型，返回一组结构化任务。
    """

    if task_type == "learning":
        tasks = [
            TaskItem(
                task_id="T1",
                title="明确学习目标",
                description="拆解学习主题、学习周期和预期成果。",
                priority="P0",
                deliverable="学习目标说明",
            ),
            TaskItem(
                task_id="T2",
                title="制定每日计划",
                description="根据学习目标生成每日学习任务和练习安排。",
                priority="P0",
                deliverable="每日学习计划",
            ),
            TaskItem(
                task_id="T3",
                title="记录学习进度",
                description="记录每日完成情况、问题和复盘内容。",
                priority="P1",
                deliverable="学习进度记录",
            ),
        ]
    elif task_type == "research":
        tasks = [
            TaskItem(
                task_id="T1",
                title="收集资料",
                description="围绕研究主题收集新闻、报告、论文或官方资料。",
                priority="P0",
                deliverable="资料清单",
            ),
            TaskItem(
                task_id="T2",
                title="提炼关键信息",
                description="对资料进行摘要、分类和信息抽取。",
                priority="P0",
                deliverable="结构化研究笔记",
            ),
            TaskItem(
                task_id="T3",
                title="形成研究结论",
                description="基于证据整理趋势判断、影响分析和不确定信息。",
                priority="P1",
                deliverable="研究结论草稿",
            ),
        ]
    elif task_type == "project":
        tasks = [
            TaskItem(
                task_id="T1",
                title="明确需求",
                description="定义项目目标、核心用户、功能范围和验收标准。",
                priority="P0",
                deliverable="需求说明文档",
            ),
            TaskItem(
                task_id="T2",
                title="搭建原型",
                description="完成最小可行版本的代码结构和核心流程。",
                priority="P0",
                deliverable="可运行 MVP",
            ),
            TaskItem(
                task_id="T3",
                title="测试与优化",
                description="测试核心功能，修复问题并整理文档。",
                priority="P1",
                deliverable="测试记录与优化清单",
            ),
        ]
    else:
        tasks = [
            TaskItem(
                task_id="T1",
                title="明确目标",
                description="梳理任务背景、目标和完成标准。",
                priority="P0",
                deliverable="目标说明",
            ),
            TaskItem(
                task_id="T2",
                title="拆解步骤",
                description="将目标拆解成可执行步骤。",
                priority="P0",
                deliverable="任务步骤清单",
            ),
            TaskItem(
                task_id="T3",
                title="执行与复盘",
                description="按步骤执行，并记录结果和改进点。",
                priority="P1",
                deliverable="执行记录与复盘",
            ),
        ]

    return TaskListResult(
        goal=goal,
        task_type=task_type,
        tasks=tasks,
    )


TOOL_DEFINITIONS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "summarize_webpage_placeholder",
            "description": "模拟总结网页内容。当前版本不会真实访问网页，只返回占位摘要。",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "需要总结的网页 URL。",
                    },
                    "focus": {
                        "type": "string",
                        "description": "摘要关注点，例如 AI 行业动态、产品发布、技术趋势。",
                    },
                },
                "required": ["url"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "generate_task_list",
            "description": "根据用户目标生成结构化任务清单。",
            "parameters": {
                "type": "object",
                "properties": {
                    "goal": {
                        "type": "string",
                        "description": "用户想要完成的目标。",
                    },
                    "task_type": {
                        "type": "string",
                        "description": "任务类型。",
                        "enum": ["learning", "project", "research", "general"],
                    },
                },
                "required": ["goal", "task_type"],
            },
        },
    },
]


TOOL_REGISTRY: dict[str, Any] = {
    "summarize_webpage_placeholder": summarize_webpage_placeholder,
    "generate_task_list": generate_task_list,
}


def run_tool(tool_name: str, arguments: dict[str, Any]) -> BaseModel:
    """根据工具名称和参数执行本地工具。"""

    if tool_name == "summarize_webpage_placeholder":
        validated_args = WebpageSummaryInput.model_validate(arguments)
        return summarize_webpage_placeholder(**validated_args.model_dump())

    if tool_name == "generate_task_list":
        validated_args = TaskListInput.model_validate(arguments)
        return generate_task_list(**validated_args.model_dump())

    raise ValueError(f"Unknown tool: {tool_name}")


def tool_result_to_json(result: BaseModel) -> str:
    """将工具结果转成 JSON 字符串。"""

    return json.dumps(
        result.model_dump(),
        ensure_ascii=False,
        indent=2,
    )


if __name__ == "__main__":
    webpage_result = summarize_webpage_placeholder(
        url="https://example.com/ai-news",
        focus="AI 行业动态",
    )
    print(tool_result_to_json(webpage_result))

    task_result = generate_task_list(
        goal="做一个 AI 学习助手",
        task_type="project",
    )
    print(tool_result_to_json(task_result))