"chama a api do brapi"
from src.logs import logger
from brapi import AsyncBrapi, NotFoundError
from src.config import SETTINGS
import pandas as pd


class BrapiTool:

    #Colunas que interessam na listagem
    COLUMNS = ["stock", "name", "close", "change", "volume", "sector", "type", "logo"]

    def __init__(self) -> None:

        self.key = SETTINGS["brapi_key"]
        self.client = AsyncBrapi(api_key=self.key)

    #Lista os ativos disponíveis (paginado)
    async def list_all(self, page: int = 1, limit: int = 50) -> list[dict]:

        logger.info(f"Listing assets (page={page}, limit={limit})...")

        try:

            resp = await self.client.quote.list(page=page, limit=limit)

            df = pd.DataFrame([s.model_dump() for s in resp.stocks])

            #reindex garante as colunas mesmo se a API não mandar alguma
            df = df.reindex(columns=self.COLUMNS)

            #NaN vira None, pra ficar JSON-friendly
            df = df.astype(object).where(df.notna(), None)

            assets = df.to_dict(orient="records")

            logger.success(f"Listed {len(assets)} assets")

            return assets

        except Exception as error:

            logger.error(f"Error: {error}")
            raise

    #Cotação de um ativo específico
    async def get_quote(self, ticker: str) -> dict:

        ticker = ticker.strip().upper()

        logger.info(f"Getting quote of {ticker}...")

        try:

            resp = await self.client.quote.retrieve(tickers=ticker)

            if not resp.results:

                logger.warning(f"{ticker} not found")
                return {"erro": f"ticker {ticker} não encontrado"}

            asset = resp.results[0]

            logger.success(f"Got quote of {ticker}")

            return {
                "ticker": asset.symbol,
                "nome": asset.short_name,
                "preco": asset.regular_market_price,
                "variacao_pct": asset.regular_market_change_percent,
                "horario": asset.regular_market_time,
            }

        except NotFoundError:

            logger.warning(f"{ticker} not found")
            return {"erro": f"ticker {ticker} não encontrado"}

        except Exception as error:

            logger.error(f"Error: {error}")
            raise
        