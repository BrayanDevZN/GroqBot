"tool de memoria"

from src.redis.control import RedisManage

class MemoryTool(RedisManage):

    def __init__(self):
        super().__init__()


    async def get_memory(self,name: str, start:int, end:int) -> list:

        """Serve pra pegar o historico de conversa de um range especifico, o parametro name é o nome da chave do redis, 
        o start é onde começa o range das conversas, o end é onde termina"""

        result = await self.get_memory(name, start, end)

        return result 

    

