from app.core.accessors import BaseAccessor
from yandex_cloud_ml_sdk._types.message import TextMessage

class TranslatedManager(BaseAccessor):
    async def translate(self, text: str) -> str:
        user_query = TextMessage(role="user", text=text)
        response = await self.store.model.run(messages=[self.store.system_prompt, user_query], timeout=self.store.config.mc.timeout)
        
        return response.alternatives[0].text
