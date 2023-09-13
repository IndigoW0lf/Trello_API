import requests
from config import trello_config

BASE_URL = "https://api.trello.com/1/"

def get_board_id(board_name):
    response = requests.get(
        f"{BASE_URL}members/me/boards?key={trello_config.API_KEY}&token={trello_config.API_TOKEN}"
    )
    boards = response.json()
    for board in boards:
        if board['name'] == board_name:
            return board['id']
    return None

def create_list(board_id, list_name):
    response = requests.post(
        f"{BASE_URL}lists?name={list_name}&idBoard={board_id}&key={trello_config.API_KEY}&token={trello_config.API_TOKEN}"
    )
    return response.json()

def create_card(list_id, card_name, desc):
    response = requests.post(
        f"{BASE_URL}cards?name={card_name}&desc={desc}&idList={list_id}&key={trello_config.API_KEY}&token={trello_config.API_TOKEN}"
    )
    return response.json()