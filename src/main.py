import asyncio
import os
import signal

from src.core.logger import setup_logger
from src.core.http_client import httpx
from src.core.scheduler import build_scheduler
from src.jobs import register_jobs


async def run():
    setup_logger()

    stop_event = asyncio.Event()

    def on_sigterm(signum, frame):  # noqa
        stop_event.set()

    signal.signal(signal.SIGTERM, on_sigterm)
    signal.signal(signal.SIGINT, on_sigterm)

    httpx.init()

    scheduler = build_scheduler()

    register_jobs(scheduler)

    scheduler.start()

    await stop_event.wait()

    os._exit(0)
