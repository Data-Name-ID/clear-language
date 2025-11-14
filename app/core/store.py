import logging


class Store:
    def __init__(self) -> None:
        from app.core.config import Config

        self.config = Config()
        self.logger = logging.getLogger("msu.store")

        # core
        from app.core.db import DatabaseAccessor
        from app.core.yc import YandexCloudManager

        self.db = DatabaseAccessor(self)
        self.yc_manager = YandexCloudManager(self)

        # managers
        from app.api.translate.manager import TranslatedManager

        self.translate_manager = TranslatedManager(self)
