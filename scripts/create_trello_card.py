import requests
from config.trello_config import API_KEY, API_TOKEN, BOARD_ID

def create_card(list_id, name, desc=None):
    url = "https://api.trello.com/1/cards"
    query = {
        'idList': list_id,
        'name': name,
        'desc': desc,
        'idBoard': BOARD_ID, 
        'key': API_KEY,
        'token': API_TOKEN
    }
    print(f"Creating card with name: {name}, in list: {list_id}")  # Add this line
    try:
        response = requests.post(url, params=query)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while creating a card: {e}")
    else:
        print(response.json())  # Print the API response
        return response.json()

def create_checklist(card_id, name):
    url = f"https://api.trello.com/1/cards/{card_id}/checklists"
    query = {
        'name': name,
        'key': API_KEY,
        'token': API_TOKEN
    }
    print(f"Creating checklist with name: {name}, on card: {card_id}")  # Add this line
    try:
        response = requests.post(url, params=query)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while creating a checklist: {e}")
    else:
        print(response.json())  # Print the API response
        return response.json()

def create_checklist_item(checklist_id, name):
    url = f"https://api.trello.com/1/checklists/{checklist_id}/checkItems"
    query = {
        'name': name,
        'key': API_KEY,
        'token': API_TOKEN
    }
    print(f"Creating checklist item with name: {name}, on checklist: {checklist_id}")  # Add this line
    try:
        response = requests.post(url, params=query)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while creating a checklist item: {e}")
    else:
        print(response.json())  # Print the API response
        return response.json()