from fastapi import APIRouter

from app.api.translate.schemas import TranslateResponse
from app.core.depends import StoreDep

router = APIRouter(prefix="/translate", tags=["Перевод на ясный язык"])


@router.get(
    "",
    summary="Запрос на перевод текста на ясный язык",
    response_description="Успешный ответ",
)
async def translate(store: StoreDep) -> TranslateResponse:
    translated_text = await store.translate_manager.translate(
        text="Исходный текст для перевода",
    )
    return TranslateResponse(translated_text=translated_text)
