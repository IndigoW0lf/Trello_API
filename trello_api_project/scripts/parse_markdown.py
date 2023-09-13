from bs4 import BeautifulSoup
import markdown2
from config.list_id_mapping import LIST_ID_MAPPING  # Importing the mapping dictionary

def parse_markdown(file_path):
    # Step 1: Read the markdown file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        list_name = lines[0].strip().split(":")[1].strip()
        list_id = LIST_ID_MAPPING.get(list_name)  # Get the list ID using the mapping
        markdown_content = ''.join(lines[1:])
    
    # Step 2: Convert markdown content to HTML
    html_content = markdown2.markdown(markdown_content)
    
    # Step 3: Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Step 4: Extract card details
    cards_details = []
    for card_section in soup.find_all('h1'):
        card_title = card_section.get_text()
        card_description = card_section.find_next('p').get_text()
        
        checklists = []
        checklist_sections = card_section.find_all_next('h2')
        
        for i, checklist_section in enumerate(checklist_sections):
            checklist_title = checklist_section.get_text()
            if i < len(checklist_sections) - 1:
                checklist_items = checklist_section.find_all_next('li', limit=checklist_sections[i+1].find_all_previous('li', limit=1000).__len__())
            else:
                checklist_items = checklist_section.find_all_next('li')
            
            checklist_items = [item.get_text() for item in checklist_items]
            checklists.append({'title': checklist_title, 'items': checklist_items})
        
        cards_details.append({
            'title': card_title,
            'description': card_description,
            'checklists': checklists
        })
    
    return list_id, cards_details
