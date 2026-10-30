"Cria conexão com redis"

from redis.asyncio import Redis
from src.logs import logger

class RedisConnection:

    def __init__(self, host:str|None=None, port:str|int|None=None, password:str|None=None, test:bool=False)->None:

        self.host = host 
        self.port = port 
        self.password = password
        self.test = test

    #Define oq as variaveis vão ser se forem None
    def _set_default(self) -> None:

        if self.test:

            self.host = "localhost"
            self.port = 6379

        else:

            self.host = self.host if self.host is not None else "redis"
            self.port = self.post if self.port is not None else 6379


    #Cria conexão com redis
    def _conn(self) -> None:

        try:

            logger.info("Creating connection with redis...")

            self.client = Redis(
                host=self.host,
                port=self.port,
                password=self.password,
                decode_responses=True
            )

        except Exception as error:

            logger.error(f"Error: {error}")
            raise 

    #Testa a conexão 3 vezes
    async def _test(self) -> None:

        countdown = 0

        while True:

            logger.info("Testing connection from redis...")

            try:

                await self.client.ping()

                logger.success("Connection ok!!")

                break 

            except Exception as error:

                if countdown != 3:

                    logger.warning(f"there was an error connecting, testing again...")
                    countdown+=1
                    continue 

                logger.error(f"Error: {error}")
                raise 

    #Executa todos os metodos e retorna conexão
    async def connect(self) -> None:

        self._set_default()
        self._conn()
        await self._test()

        




        