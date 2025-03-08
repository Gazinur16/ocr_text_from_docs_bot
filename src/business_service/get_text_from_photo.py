import base64
from mistralai import Mistral

from src.core.settings import get_settings


settings = get_settings()
client = Mistral(api_key=settings.mistral_api_key)

async def get_text_from_photo(*, file_bytes: bytes, file_type: str) -> str:
    base64_image = base64.b64encode(file_bytes).decode("utf-8")
    type_photo = "image/png" if file_type == "png" else "image/jpeg"
    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={"type": "image_url",
                  "image_url": f"data:{type_photo};base64,{base64_image}"},
    )

    full_text = "\n".join(page.markdown for page in ocr_response.pages)
    return full_text