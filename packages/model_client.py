import os
from typing import Generator, Literal, Optional

from dotenv import load_dotenv
from openai import OpenAI


ModelType = Literal["default", "flash", "pro"]


class ModelClient:
    """统一封装 LLM API 调用，支持 default / flash / pro 三类模型选择。"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        default_model: Optional[str] = None,
        flash_model: Optional[str] = None,
        pro_model: Optional[str] = None,
    ) -> None:
        load_dotenv()

        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("BASE_URL") or None

        self.default_model = default_model or os.getenv("DEFAULT_MODEL")
        self.flash_model = flash_model or os.getenv("FLASH_MODEL") or self.default_model
        self.pro_model = pro_model or os.getenv("PRO_MODEL") or self.default_model

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

        if not self.default_model:
            raise ValueError("DEFAULT_MODEL is not set. Please check your .env file.")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )

    def _select_model(self, model_type: ModelType = "default") -> str:
        """根据任务类型选择模型。"""

        if model_type == "default":
            return self.default_model

        if model_type == "flash":
            return self.flash_model

        if model_type == "pro":
            return self.pro_model

        raise ValueError(
            f"Unsupported model_type: {model_type}. "
            "Expected one of: default, flash, pro."
        )

    def chat(
        self,
        user_message: str,
        system_message: str = "你是一个专业、清晰、可靠的 AI 助手。",
        temperature: float = 0.3,
        model_type: ModelType = "default",
    ) -> str:
        """普通文本调用：输入用户消息，返回完整文本。"""

        selected_model = self._select_model(model_type)

        response = self.client.chat.completions.create(
            model=selected_model,
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            temperature=temperature,
        )

        content = response.choices[0].message.content

        if content is None:
            return ""

        return content

    def stream_chat(
        self,
        user_message: str,
        system_message: str = "你是一个专业、清晰、可靠的 AI 助手。",
        temperature: float = 0.3,
        model_type: ModelType = "default",
    ) -> Generator[str, None, None]:
        """流式文本调用：边生成边返回文本片段。"""

        selected_model = self._select_model(model_type)

        stream = self.client.chat.completions.create(
            model=selected_model,
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            temperature=temperature,
            stream=True,
        )

        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta


if __name__ == "__main__":
    client = ModelClient()

    print("=== Default Model Test ===")
    result = client.chat(
        "用三句话解释什么是 Prompt Engineering。",
        model_type="default",
    )
    print(result)

    print("\n=== Flash Model Test ===")
    result = client.chat(
        "用三句话解释什么是结构化输出。",
        model_type="flash",
    )
    print(result)

    print("\n=== Pro Model Test ===")
    result = client.chat(
        "请从技术、产品、工程化三个角度分析 LLM API 封装在 AI 应用开发中的价值。",
        model_type="pro",
    )
    print(result)

    print("\n=== Streaming Flash Model Test ===")
    for chunk in client.stream_chat(
        "用三句话解释什么是流式输出。",
        model_type="flash",
    ):
        print(chunk, end="", flush=True)

    print()