from loguru import logger
import sys
from app.core.config import settings

def setup_logging():
    logger.remove()
    logger.add(
        sys.stdout,
        level=settings.log_level,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level}</level> | "
            "<cyan>{name}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
    )

    return logger
