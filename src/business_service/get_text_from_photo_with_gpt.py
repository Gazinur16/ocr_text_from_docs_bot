import logging
import base64
from openai import OpenAI
from src.core.const import PROMPT_TO_EXTRACT_TEXT_FROM_PHOTO
from src.core.settings import get_settings

settings = get_settings()
_logger = logging.getLogger(__name__)

client = OpenAI(
    api_key=settings.openai_api_key,
    base_url=settings.openai_api_base_url
)

async def get_text_from_photo_with_gpt(file_bytes: bytes) -> str | None:
    try:
        image_base64 = base64.b64encode(file_bytes).decode("utf-8")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": PROMPT_TO_EXTRACT_TEXT_FROM_PHOTO},
                {"role": "user", "content": [
                    {"type": "text", "text": "Извлеки весь текст из фото"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
                ]}
            ],
            max_tokens=300
        )

        raw_response = response.choices[0].message.content.strip()

        if not raw_response:
            return None

        return raw_response

    except Exception as e:
        _logger.error(e)
        return None
