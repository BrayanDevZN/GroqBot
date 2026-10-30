"Teste de brapi"

from src.tools.brapi import BrapiTool
import asyncio

async def test_brapi() -> None:

    brapi = BrapiTool()

    todas = await brapi.list_all(page=1, limit=5)

    print(len(todas))
    print(todas[0])

    print(await brapi.get_quote("petr4"))

    print(await brapi.get_quote("XXXX9"))


if __name__ == "__main__":
    asyncio.run(test_brapi())