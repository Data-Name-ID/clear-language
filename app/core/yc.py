from yandex_cloud_ml_sdk import AsyncYCloudML
from yandex_cloud_ml_sdk._types.message import TextMessage
from yandex_cloud_ml_sdk.auth import OAuthTokenAuth

from app.core.accessors import BaseAccessor
from app.core.store import Store


class YandexCloudManager(BaseAccessor):
    def __init__(self, store: Store) -> None:
        super().__init__(store)

        _auth = OAuthTokenAuth(self.store.config.yc.oauth_token)
        _ya_sdk = AsyncYCloudML(
            folder_id=self.store.config.yc.folder_id,
            auth=_auth,
        )
        self.system_prompt = TextMessage(
            role="system",
            text=self.store.config.mc.instruction,
        )

        self.model = _ya_sdk.models.completions(self.store.config.yc.model_name)
        self.model = self.model.configure(
            temperature=self.store.config.mc.temperature,
            max_tokens=self.store.config.mc.max_tokens,
        )
