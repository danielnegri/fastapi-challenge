import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app import storage
from app.core.config import settings
from app.models.session import SessionLocal
from app.schemas import UserCreate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 20  # 20 seconds
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        # Try to create session to check if DB is awake
        db = SessionLocal()
        db.execute("SELECT 1")

        # Initialize super user
        superuser = storage.users.get_by_email(db, email=settings.ADMIN_EMAIL)
        if not superuser:
            user_in = UserCreate(
                email=settings.ADMIN_EMAIL,
                password=settings.ADMIN_PASSWORD,
                full_name="Administrator",
                is_superuser=True,
            )
            storage.users.create(db, obj_in=user_in)

        db.close()
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
