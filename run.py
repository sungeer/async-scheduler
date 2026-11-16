import asyncio

from src.main import run

try:
    asyncio.run(run())
except KeyboardInterrupt:
    pass
