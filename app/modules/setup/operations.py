import json
from app.constants import SETUP_FILE
from .typing import SetupData


def get_data() -> SetupData:
    with open(SETUP_FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
