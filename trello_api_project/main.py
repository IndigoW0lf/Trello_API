import requests
from config import trello_config
import json
from scripts.create_trello_card import create_card, get_card, create_checklist

API_KEY = "API_KEY"
TOKEN = "TOKEN"

BASE_URL = "https://api.trello.com/1"

if __name__ == "__main__":
    # Replace 'list_id_here' with the actual list ID and 'Card Name' with the desired card name
    card_response = create_card('list_id_here', 'Card Name', 'Card Description')
    card_id = card_response['id']

    # Getting card details
    card_details = get_card(card_id)
    print(json.dumps(card_details, indent=4))

    # Creating a checklist on the card
    checklist_response = create_checklist(card_id, 'Checklist Name')
    print(json.dumps(checklist_response, indent=4))
