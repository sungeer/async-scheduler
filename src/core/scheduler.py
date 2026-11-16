from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src import settings


def build_scheduler() -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler(
        executors={
            'default': AsyncIOExecutor(),
        },
        job_defaults={
            'max_instances': 1,
            'coalesce': True,
            'misfire_grace_time': settings.MISFIRE_GRACE_TIME,
        },
        timezone=settings.TIMEZONE,
    )
    return scheduler
