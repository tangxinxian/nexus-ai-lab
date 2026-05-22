from typing import List, Literal, Optional
from pydantic import BaseModel, Field, ValidationError


class SummaryResult(BaseModel):
    """行业信息总结结果。"""

    summary: str = Field(description="一句话总结")
    key_points: List[str] = Field(description="关键信息列表")
    entities: List[str] = Field(default_factory=list, description="涉及的公司、产品、技术等实体")
    uncertainties: List[str] = Field(default_factory=list, description="原文未提及或无法确认的信息")


class ClassifyResult(BaseModel):
    """行业信息分类结果。"""

    category: Literal[
        "技术突破",
        "产品发布",
        "融资并购",
        "政策监管",
        "市场竞争",
        "商业合作",
        "其他",
    ] = Field(description="行业信息分类标签")
    confidence: float = Field(ge=0, le=1, description="分类置信度，范围 0-1")
    reason: str = Field(description="分类理由")


class ExtractResult(BaseModel):
    """行业信息抽取结果。"""

    companies: List[str] = Field(default_factory=list, description="公司或机构")
    products: List[str] = Field(default_factory=list, description="产品名称")
    technologies: List[str] = Field(default_factory=list, description="技术关键词")
    metrics: List[str] = Field(default_factory=list, description="关键指标，如速度、金额、比例等")
    dates: List[str] = Field(default_factory=list, description="日期信息")


def parse_summary(data: dict) -> SummaryResult:
    """解析并校验总结结果。"""
    return SummaryResult.model_validate(data)


def parse_classify(data: dict) -> ClassifyResult:
    """解析并校验分类结果。"""
    return ClassifyResult.model_validate(data)


def parse_extract(data: dict) -> ExtractResult:
    """解析并校验抽取结果。"""
    return ExtractResult.model_validate(data)


def safe_parse_summary(data: dict) -> Optional[SummaryResult]:
    """安全解析总结结果，失败时返回 None。"""
    try:
        return parse_summary(data)
    except ValidationError as error:
        print("SummaryResult validation failed:")
        print(error)
        return None


def safe_parse_classify(data: dict) -> Optional[ClassifyResult]:
    """安全解析分类结果，失败时返回 None。"""
    try:
        return parse_classify(data)
    except ValidationError as error:
        print("ClassifyResult validation failed:")
        print(error)
        return None


def safe_parse_extract(data: dict) -> Optional[ExtractResult]:
    """安全解析抽取结果，失败时返回 None。"""
    try:
        return parse_extract(data)
    except ValidationError as error:
        print("ExtractResult validation failed:")
        print(error)
        return None


if __name__ == "__main__":
    summary_data = {
        "summary": "智谱发布 GLM-5.1 高速版，带动港股 AI 应用股走强。",
        "key_points": [
            "GLM-5.1-HighSpeed 输出速度达到 400 Tokens/s",
            "该 API 面向部分企业客户开放",
            "适用于 AI 编程、实时交互、商业决策等低延迟场景",
        ],
        "entities": ["智谱", "GLM-5.1-HighSpeed", "MiniMax"],
        "uncertainties": ["原文未提及具体定价和全面开放时间"],
    }

    classify_data = {
        "category": "产品发布",
        "confidence": 0.92,
        "reason": "文本核心事件是智谱发布 GLM-5.1 高速版 API。",
    }

    extract_data = {
        "companies": ["智谱", "MiniMax"],
        "products": ["GLM-5.1高速版", "GLM-5.1-HighSpeed API"],
        "technologies": ["大模型 API", "低延迟推理"],
        "metrics": ["400 Tokens/s", "盘中涨超32%", "盘中涨超20%"],
        "dates": ["5月22日"],
    }

    print(parse_summary(summary_data))
    print(parse_classify(classify_data))
    print(parse_extract(extract_data))

    # print("\n--- Bad classify data test ---")

    # bad_classify_data = {
    #     "category": "股价上涨",
    #     "confidence": 1.2,
    #     "reason": "测试错误数据",
    # }

    # result = safe_parse_classify(bad_classify_data)
    # print(result)

    # print("\n--- Bad summary data test ---")

    # bad_summary_data = {
    #     "summary": "智谱发布高速版 API。"
    # }

    # result = safe_parse_summary(bad_summary_data)
    # print(result)