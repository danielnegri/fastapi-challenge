from fastapi import APIRouter

from app.api.v1.endpoints import auth, loans, users

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(loans.router, prefix="/loans", tags=["loan"])
router.include_router(users.router, prefix="/users", tags=["users"])
