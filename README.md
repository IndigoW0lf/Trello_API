
---

# Trello API Project

## Introduction

I've been thoroughly enjoying the help I get from ChatGPT on my projects. It effortlessly keeps up with my project details, workflow, bugs, and current issues, and has really helped me with project management for a big project I'm working on. As I was working on my Trello cards and to-do lists, I realized that manually copying and pasting individual checklist items was becoming quite tedious. So, I decided to create this script to help automate the creation of kanban cards on Trello, making the entire process smoother and more efficient!

## About the Project

This project is a Python script that parses a markdown file with a specific syntax to create cards, checklists, and checklist items on Trello. It utilizes the Trello API to automate the process of creating and managing Trello cards, making project management a breeze!

## Setting Up

To get this project up and running on your system, make sure you have a code editor/IDE that plays nicely with python, and follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine.
   
2. **Create a Virtual Environment:** Navigate to the project directory and create a virtual environment using the following command:

   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment:** 

   - On Windows:
     
     ```bash
     .\venv\Scripts\activate
     ```

   - On Unix or MacOS:
     
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:** Install the necessary dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

5. **Create a .gitignore File:** Before moving forward, create a `.gitignore` file in your project root directory to avoid pushing sensitive data to your repository. Add the following line to it:

   ```
   trello_config.py
   ```

6. **Get Trello API Key:** You will need to get an API key from Trello. Create a new Trello power-up to get your API key. For the required URL field, you can use a placeholder like `http://example.com`. Detailed steps can be found in the [Trello API Documentation](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

7. **Setup Configuration File:** Create a `trello_config.py` file inside the `config` folder to store sensitive variables such as your API key and token. After getting your API key, you can obtain your token by visiting the following URL:

   ```
   https://trello.com/1/authorize?expiration=1day&name=MyPersonalToken&scope=read,write&response_type=token&key=YOUR_API_KEY_HERE
   ```

   Replace `YOUR_API_KEY_HERE` with the API key you obtained in step 6. This will guide you through a process to grant access and retrieve your token.

   Here's a sample setup for the `trello_config.py`:

   ```python
   API_KEY = 'your_trello_api_key'
   API_TOKEN = 'your_trello_api_token'
   BOARD_ID = 'your_trello_board_id'
   ```

8. **Get Board and List Details:** To get your board ID, you can find it in the URL of your Trello board. The URL structure is usually `https://trello.com/b/YOUR_BOARD_ID/your-board-name`. Once you have your board ID, use the `get_list_details` function (explained in the next section) to retrieve the IDs of your lists. Copy this information into the `list_id_mapping.py` file in your `config` folder.

9. **Edit the Markdown File:** You can edit the `trello_test.md` file in the project directory to include your tasks, checklists, and checklist items following the syntax shown in the file. This is the file that the script will parse to create cards on Trello.

10. **Run the Script:** Now, you are all set to run the main script that parses the markdown file and creates cards on Trello. Use the following command in your command line to run it:

   ```bash
   python main.py
   ```

### Getting List Details

This is a thorough explanation of step #8

To get the list details, use the following script which should be saved as `get_list_details.py`:

```python
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
    
    return list_id_mapping

if __name__ == "__main__":
    print(get_list_details())
```

To run the above script and get your list details, use the following command:

```bash
python get_list_details.py
```

This will print the names and IDs of your lists, which you can then copy into `list_id_mapping.py`.

Here's an example of what this will look like, make sure to name the LIST_ID_MAPPING variable exactly the same way.

```bash
LIST_ID_MAPPING = {
  'Project Resources': 'your_ProjectResources_list_id', 
  'Backlog': 'your_Backlog_list_id', 
  'To Do': 'your_ToDo_list_id', 
  'In Progress': 'your_InProgress_list_id',
  }
```
Don't forget to go back to step #9 now!

## Future Developments

As we further develop this project, it would be beneficial to include functionalities such as:

- Adding labels,  to the cards.
- Updating existing cards and checklists.
- Expanding the script to manage more aspects of Trello boards and lists.

Feel free to fork the project and propose new features, or contribute in any way you see fit!

## Conclusion

This script is designed to facilitate a smoother and more efficient project management experience with Trello. It's open-source, and contributions to enhance its capabilities are welcome. Together, we can make project management a seamless experience!
