import logging

from yandex_cloud_ml_sdk import AsyncYCloudML


class Store:
    def __init__(self) -> None:
        from app.core.config import Config

        self.config = Config()
        self.logger = logging.getLogger("msu.store")

        # core
        from app.core.db import DatabaseAccessor

        self.db = DatabaseAccessor(self)
        self.ya_sdk = AsyncYCloudML(
            folder_id="<идентификатор_каталога>",
            auth="<API-ключ>",
        )

        # managers
        from app.api.translate.manager import TranslatedManager

        self.translate_manager = TranslatedManager(self)
