import requests
from config.trello_config import API_KEY, API_TOKEN, BOARD_ID

def get_list_details():
    url = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': API_KEY,
        'token': API_TOKEN
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

    lists_details = response.json()
    list_id_mapping = {list_detail['name']: list_detail['id'] for list_detail in lists_details}
    print(list_id_mapping)

if __name__ == "__main__":
    get_list_details()