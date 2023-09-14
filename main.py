from scripts.create_trello_card import create_card, create_checklist, create_checklist_item
from scripts.parse_markdown import parse_markdown 

def main():
    print("Starting script...")
    # Step 1: Parse the markdown file to get the list ID and card details
    list_id, cards_details = parse_markdown('markdown_files/xml.md')

    # Step 2: Loop through each card's details and create cards and checklists on Trello
    for card_details in cards_details:
        card_title = card_details['title']
        card_description = card_details['description']
        
        # Step 2.1: Create a card on Trello
        response = create_card(list_id, card_title, card_description)
        card_id = response['id']

        for checklist in card_details['checklists']:
            checklist_name = checklist['title']
            checklist_response = create_checklist(card_id, checklist_name)
            checklist_id = checklist_response['id']  # Get the ID of the created checklist

            # Loop through checklist['items'] to add each item to the checklist
            for item in checklist['items']:
                create_checklist_item(checklist_id, item)

    print("Cards and checklists created successfully.")

if __name__ == "__main__":
    main()

