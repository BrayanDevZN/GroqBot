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
    load_dotenv(BASE_DIR)


NAMES = ["groq_key", "telegram_token"]
SETTINGS = {}
for name in NAMES:

    env = os.getenv(name)

    if env is None:
        raise NotFoundEnv(f"Expeted env {name}")

    SETTINGS[name] = env 



    

    




