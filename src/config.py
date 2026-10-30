"pega as variaveis de ambiente"
from pathlib import Path 
from dotenv import load_dotenv
import os 

class NotFoundEnv(Exception):
    pass 

BASE_DIR = Path(__file__).resolve().parent.parent
if  os.path.exists(BASE_DIR / ".env"):
    load_dotenv(BASE_DIR / ".env")

else:
    load_dotenv()


REQUIRED_NAMES = ["brapi_key"]
SETTINGS = {}
for name in REQUIRED_NAMES:

    env = os.getenv(name)

    if env is None:
        raise NotFoundEnv(f"Expeted env {name}")

    SETTINGS[name] = env 


NAMES = ["redis_port", "redis_host", "redis_password", "test", "telegram_token", "groq_key"]
for name in NAMES:
    env = os.getenv(name)
    SETTINGS[name] = env




    

    




