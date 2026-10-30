"tool de memoria"
from .schema import tool
from src.redis.control import RedisManage


class MemotryTool(RedisManage):

    def __init__(self, host = None, port = None, password = None, test = False):
        super().__init__(host, port, password, test)


    async def 

