from app.core.accessors import BaseAccessor


class TranslatedManager(BaseAccessor):
    async def translate(self, text: str) -> str:
        return "Пример переведенного текста"
