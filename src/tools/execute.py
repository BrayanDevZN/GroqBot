"Agrupa as tools e cria elas para integração"

from .schema import tool_schema
from .brapi import ActionsTool
from .memory import MemoryTool
from typing import Any
class GroupTools(ActionsTool, MemoryTool):

    def __init__(self)->None:

        self.methods = [self.get_active, self.get_all, self.get_memory]
        self.tools = {}
        self._transform_tools()

        super().__init__()


    #Transforma os metodos em tools
    def _transform_tools(self) -> None:

      
        for method in self.methods:

            tool = tool_schema(func=method)

            self.tools[tool["function"]["name"]] = {
                "metadata": tool,
                "function": method
            }

    #Pega os dados das tools
    def get_metadata(self) -> list[dict]:

        metadata = []

        for tool in self.tools.values():

            metadata.append(tool["metadata"])

        return metadata



            

    #Executa a tool
    async def execute(self, name:str, args:dict) -> Any:

        if name in self.tools.keys():

            tool = self.tools[name]
            function = tool["function"]

            result = await function(**args)

            return result

        return None  



      










        