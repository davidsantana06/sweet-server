import json
from app.config import paths
from .typing import SetupData


def get_data() -> SetupData:
    with open(paths.SETUP_FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
