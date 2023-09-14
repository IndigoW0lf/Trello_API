
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

6: **Create and Activate a Trello Power-Up**

   To access the Trello API, you'll need to create a Power-Up. Follow these steps to set up and activate your Power-Up:
   
   1. Visit the [Trello Power-Up administration page](https://trello.com/power-ups/admin).
   2. Click on the 'Create New Power-Up' button.
   3. If it is your first time creating a power-up, you might need to agree to Trello's API terms of service.
   4. You will be presented with a form to create your new Power-Up. Here's how to fill in some of the fields:
      - **Name**: Give your Power-Up a name (e.g., My Trello API Power-Up).
      - **Author**: Your name or your organization's name.
      - **Email**: Your contact email.
      - **Overview**: A brief description of what your Power-Up does (or not, lol).
      - **Description**: A detailed description of your Power-Up (or leave blank like I did).
      - **Icon URL**: You can leave this blank or put any image URL.
      - **Iframe Connector URL**: Here, you can put any URL (e.g., https://example.com) since it's not used in this project.
   5. Click 'Save' to create your Power-Up.
   6. Now, note down the API key. You can generate a token by visiting the following URL, replacing `YOUR_API_KEY_HERE` with the API key you just noted down:
   
   ```
   https://trello.com/1/authorize?expiration=1day&name=MyPersonalToken&scope=read,write&response_type=token&key=YOUR_API_KEY_HERE
   ```

7. **Activate Your Power-Up**: Go to your Trello board and click on the 'Power Ups' button (usually found on the top right corner). Hit the blue 'Add Powerups' button. To the left click the 'custom' section, find and activate the Power-Up you just created.

Remember to store your API key and token in the `config/trello_config.py` file. This file should look something like this:

```python
API_KEY = "your_api_key_here"
API_TOKEN = "your_api_token_here"
BOARD_ID = "your_board_id_here"
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
