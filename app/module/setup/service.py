import json
from app.config import path
from .typing import SetupData


def get_data() -> SetupData:
    with open(path.SETUP_FILE, encoding='utf-8') as file:
        return json.load(file)
