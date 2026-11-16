import logging

logger = logging.getLogger(__name__)


# 示例任务 每 3 分钟跑一次
async def task_a():
    logger.info('run task_a')


async def task_b():
    logger.info('run task_b')


async def task_c():
    logger.info('run task_c')
