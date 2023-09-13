from bs4 import BeautifulSoup
import markdown2
from config.list_id_mapping import LIST_ID_MAPPING

def parse_markdown(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        list_name = lines[0].strip().split(":")[1].strip()
        list_id = LIST_ID_MAPPING.get(list_name)
        markdown_content = ''.join(lines[1:])
        print(f"List Name: {list_name}, List ID: {list_id}")
    
    html_content = markdown2.markdown(markdown_content)
    print(html_content)
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    cards_details = []
    for card_section in soup.find_all('h2'):
        card_title = card_section.get_text()
        card_description = card_section.find_next('p').get_text()

        checklists = []
        checklist_sections = card_section.find_all_next('h3')

        for checklist_section in checklist_sections:
            checklist_title = checklist_section.get_text()

            # Find the parent card section of the current checklist section
            parent_card_section = checklist_section.find_all_previous('h2')
            if parent_card_section:
                parent_card_section = parent_card_section[0]

            # If the parent card section is not the current card section, we skip this iteration
            if parent_card_section != card_section:
                continue

            checklist_items = checklist_section.find_next('ul').find_all('li')
            checklist_items = [item.get_text() for item in checklist_items]
            checklists.append({'title': checklist_title, 'items': checklist_items})

        cards_details.append({
            'title': card_title,
            'description': card_description,
            'checklists': checklists
        })

    return list_id, cards_details
