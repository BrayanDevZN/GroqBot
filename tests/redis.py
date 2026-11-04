"Testa o redis"

from src.redis.control import RedisManage
import asyncio

async def test_redis() -> None:

    redis = RedisManage()

    await redis.connect()

    await redis.insert("chat:teste", ["a", "b", "c"], expires=60)

    print(await redis.get_range("chat:teste", 0, -1))

    await redis.delete("chat:teste")

    print(await redis.get_range("chat:teste", 0, -1))


if __name__ == "__main__":
    asyncio.run(test_redis())