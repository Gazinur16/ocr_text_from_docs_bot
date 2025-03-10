import base64
from mistralai import Mistral

from src.core.settings import get_settings


settings = get_settings()
client = Mistral(api_key=settings.mistral_api_key)

async def get_text_from_pdf_doc_with_gpt(file_bytes: bytes) -> str | None:
    uploaded_pdf = client.files.upload(
        file={"file_name": "document.pdf", "content": file_bytes},
        purpose="ocr",
    )

    signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)
    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={"type": "document_url",
                  "document_url": signed_url.url},
    )

    result_text = "\n".join(page.markdown for page in ocr_response.pages)
    return result_text if result_text.strip() else None