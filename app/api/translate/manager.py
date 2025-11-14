from yandex_cloud_ml_sdk._types.message import TextMessage

from app.core.accessors import BaseAccessor


class TranslatedManager(BaseAccessor):
    async def translate(self, text: str) -> str:
        user_query = TextMessage(role="user", text=text)
        response = await self.store.yc_manager.model.run(
            messages=[self.store.yc_manager.system_prompt, user_query],
            timeout=self.store.config.mc.timeout,
        )

        return response.alternatives[0].text
