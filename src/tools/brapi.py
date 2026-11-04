"tool de brapi"

from src.brapi import BrapiTool

class ActionsTool(BrapiTool):

    def __init__(self):
        super().__init__()

    async def get_all(self, page: int = 1, limit: int = 50) -> list[dict]:

        """Lista todos os ativos disponiveis, page e o limite de paginas, e limit é o limite de ativos"""

        return await self.list_all(page, limit)


    async def get_active(self, ticker:str) -> dict:

        """Pega um ativo especifico, o ticker é o ticker do ativo que voce quer"""

        return self.get_quote(ticker)


    