from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from packages.model_client import ModelClient
from packages.tools import generate_task_list


app = FastAPI(
    title="Nexus Base Assistant API",
    description="Nexus AI Lab W1 FastAPI Demo，提供 chat、summarize、plan 三类 AI 能力接口。",
    version="0.1.0",
)

model_client = ModelClient()


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class ChatRequest(BaseModel):
    message: str = Field(description="用户输入消息")
    model_type: Literal["default", "flash", "pro"] = Field(
        default="flash",
        description="模型类型：default / flash / pro",
    )
    temperature: float = Field(
        default=0.3,
        ge=0,
        le=2,
        description="模型输出随机性",
    )


class ChatResponse(BaseModel):
    reply: str
    model_type: str


class SummarizeRequest(BaseModel):
    text: str = Field(description="需要总结的行业文本")
    model_type: Literal["default", "flash", "pro"] = Field(
        default="flash",
        description="模型类型：default / flash / pro",
    )


class SummarizeResponse(BaseModel):
    summary: str
    model_type: str


class PlanRequest(BaseModel):
    goal: str = Field(description="用户目标")
    task_type: Literal["learning", "project", "research", "general"] = Field(
        default="project",
        description="任务类型",
    )


class TaskItemResponse(BaseModel):
    task_id: str
    title: str
    description: str
    priority: Literal["P0", "P1", "P2"]
    deliverable: str


class PlanResponse(BaseModel):
    goal: str
    task_type: str
    tasks: list[TaskItemResponse]


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """健康检查接口。"""

    return HealthResponse(
        status="ok",
        service="Nexus Base Assistant API",
        version="0.1.0",
    )


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """普通 AI 对话接口。"""

    try:
        reply = model_client.chat(
            user_message=request.message,
            system_message="你是 Nexus Base Assistant，一个专业、清晰、可靠的 AI 应用开发助手。",
            temperature=request.temperature,
            model_type=request.model_type,
        )

        return ChatResponse(
            reply=reply,
            model_type=request.model_type,
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Model call failed: {error}",
        ) from error


@app.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest) -> SummarizeResponse:
    """行业信息总结接口。"""

    prompt = f"""
你是一个 AI 行业研究分析师。

请对以下行业文本进行结构化总结，要求简洁、专业，不要编造原文没有的信息。

文本如下：

\"\"\"
{request.text}
\"\"\"

请输出：

## 一句话总结

## 关键信息
- 
- 
- 

## 可能影响
- 对行业：
- 对公司：
- 对用户/客户：

## 不确定信息
- 
"""

    try:
        summary = model_client.chat(
            user_message=prompt,
            system_message="你是一个严谨的 AI 行业研究助手，只基于输入文本进行分析。",
            temperature=0.2,
            model_type=request.model_type,
        )

        return SummarizeResponse(
            summary=summary,
            model_type=request.model_type,
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Summarize failed: {error}",
        ) from error


@app.post("/plan", response_model=PlanResponse)
def plan(request: PlanRequest) -> PlanResponse:
    """任务拆解接口。

    该接口先直接调用本地工具 generate_task_list。
    D5 已验证模型可通过 Tool Calls 选择该工具；
    D6 先将其封装为稳定 API。
    """

    try:
        result = generate_task_list(
            goal=request.goal,
            task_type=request.task_type,
        )

        return PlanResponse(
            goal=result.goal,
            task_type=result.task_type,
            tasks=[
                TaskItemResponse(
                    task_id=task.task_id,
                    title=task.title,
                    description=task.description,
                    priority=task.priority,
                    deliverable=task.deliverable,
                )
                for task in result.tasks
            ],
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Plan generation failed: {error}",
        ) from error