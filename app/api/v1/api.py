from fastapi import APIRouter

from app.api.v1.endpoints import auth, loans, schedule, users

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(loans.router, prefix="/loans", tags=["loan"])
router.include_router(
    schedule.router, prefix="/loans/{loan_id}/schedule", tags=["schedules"]
)
router.include_router(users.router, prefix="/users", tags=["users"])
