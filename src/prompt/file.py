"Le o arquivo do prompt"

from pathlib import Path 
import os
BASE_DIR = Path(__file__).resolve().parent / "prompt.md"

if not os.path.exists(BASE_DIR):
    raise FileNotFoundError(f"Expeted {BASE_DIR}")

with open(BASE_DIR, "r", encoding="utf-8") as file:

    prompt = file.read()


class EmptyError(Exception):
    pass 

if len(prompt) == 0:

    raise EmptyError(f"Empty content in {BASE_DIR}")

