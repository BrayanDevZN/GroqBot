"Faz as operações com redis"
from .connect import logger, RedisConnection

from redis import WatchError

class RedisManage(RedisConnection):

    def __init__(self, host:str|None = None, port:str|int|None = None, 
                 password:str|None = None, test:bool = False)->None:

        super().__init__(host, port, password, test)

       

    #Insere na lsita
    async def insert(self, name:str, value:list|dict, expires: int|None = None) -> None:

        while True:

            try:

                logger.info(f"Inserting in {name}...")

                async with self.client.pipeline(transaction=True) as client:

                    await client.watch(name)
                    client.multi()
                    client.rpush(name, value) if not isinstance(value, list) else client.rpush(name, *value)

                    if expires is not None:

                        client.expire(name=name, time=expires)

                    await client.execute()

                    logger.success(f"Inserted in {name} with sucess")

                    break

            except WatchError:

                logger.warning(f"Someone was already trying to change {name}")
                continue 

    #Le num range especifico
    async def get_range(self, name:str, start:int, end:int) -> list:

        

        while True:

            try:

                logger.info(f"Geting in {name}...")

                async with self.client.pipeline(transaction=True) as client:

                    await client.watch(name)
                    client.multi()
                    client.lrange(name=name, start=start, end=end)
                    
                   
                    result = await client.execute()

                    return result[0]

            except WatchError:

                logger.warning(f"Someone was already trying to change {name}")
                continue

    #Deleta 
    async def delete(self, name:str) -> None:

        logger.info(f"Deleting {name}...")

        try:

            async with self.client.pipeline() as client:

                client.delete(name)
                await client.execute()

        except Exception as error:

            logger.error(f"Error: {error}")
            raise



        

        


    