from fastapi import APIRouter

from app.api.translate.schemas import TranslateResponse

router = APIRouter(prefix="/translate", tags=["Перевод на ясный язык"])


@router.get(
    "",
    summary="Запрос на перевод текста на ясный язык",
    response_description="Успешный ответ",
)
async def translate() -> TranslateResponse:
    return TranslateResponse(translated_text="Пример переведенного текста")
