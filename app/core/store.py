import logging

from yandex_cloud_ml_sdk import AsyncYCloudML
from yandex_cloud_ml_sdk._types.message import TextMessage

from yandex_cloud_ml_sdk.auth import OAuthTokenAuth
class Store:
    def __init__(self) -> None:
        from app.core.config import Config

        self.config = Config()
        self.logger = logging.getLogger("msu.store")

        # core
        from app.core.db import DatabaseAccessor

        self.db = DatabaseAccessor(self)
        
        # yc client
        _auth = OAuthTokenAuth(self.config.yc.oauth_token)
        _ya_sdk = AsyncYCloudML(
            folder_id=self.config.yc.folder_id,
            auth=_auth,
        )
        self.system_prompt = TextMessage(role="system", text= self.config.mc.instruction)

        self.model = _ya_sdk.models.completions(self.config.yc.model_name)
        self.model = self.model.configure(temperature=self.config.mc.temperature, max_tokens=self.config.mc.max_tokens)

        # managers
        from app.api.translate.manager import TranslatedManager

        self.translate_manager = TranslatedManager(self)
