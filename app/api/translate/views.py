from fastapi import APIRouter

from app.api.translate.schemas import TranslateRequest, TranslateResponse
from app.core.depends import StoreDep

router = APIRouter(prefix="/translate", tags=["Перевод на ясный язык"])


@router.get(
    "",
    summary="Запрос на перевод текста на ясный язык",
    response_description="Успешный ответ",
)
async def translate(store: StoreDep, data: TranslateRequest) -> TranslateResponse:
    translated_text = await store.translate_manager.translate(text=data.text)
    return TranslateResponse(translated_text=translated_text)
