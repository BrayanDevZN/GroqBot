"Teste das tools"

from src.tools.execute import GroupTools
import asyncio

async def test_tools() -> None:

    instance = GroupTools()
    tools = instance.get_metadata()
    print(tools)

    executions = [
        {
            "name": "get_all",
            "args": {"page": 2, "limit": 3}
        }
    ]

    for execution in executions:

        result = await instance.execute(name=execution["name"], args=execution["args"])
        print(result)

    



if __name__ == "__main__":
    asyncio.run(test_tools())