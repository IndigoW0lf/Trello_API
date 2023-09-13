import requests
import json
from config import API_KEY, API_TOKEN, BOARD_ID


def create_card(list_id, name, desc=None):
    url = "https://api.trello.com/1/cards"
    query = {
        'idList': list_id,
        'name': name,
        'desc': desc,
        'key': API_KEY,
        'token': API_TOKEN
    }
    response = requests.post(url, params=query)
    return response.json()

def get_card(card_id):
    url = f"https://api.trello.com/1/cards/{card_id}"
    query = {
        'key': API_KEY,
        'token': API_TOKEN
    }
    response = requests.get(url, params=query)
    return response.json()

def create_checklist(card_id, name):
    url = f"https://api.trello.com/1/cards/{card_id}/checklists"
    query = {
        'name': name,
        'key': API_KEY,
        'token': API_TOKEN
    }
    response = requests.post(url, params=query)
    return response.json()

