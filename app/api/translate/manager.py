from app.core.accessors import BaseAccessor


class UserManager(BaseAccessor):
    async def translate(self, text: str) -> str:
        pass
