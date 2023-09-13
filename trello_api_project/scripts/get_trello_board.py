import requests
import json
from trello_api_project.config.trello_config import API_KEY, API_TOKEN, BOARD_ID

url = f"https://api.trello.com/1/boards/{BOARD_ID}"

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

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
