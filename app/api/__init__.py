from fastapi import APIRouter

from app.api.ping.views import router as ping_router
from app.api.translate.views import router as translate_router

router = APIRouter(prefix="/api")

router.include_router(ping_router)
router.include_router(translate_router)
