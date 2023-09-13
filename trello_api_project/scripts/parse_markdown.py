from bs4 import BeautifulSoup
import markdown2

def parse_markdown(file_path):
    # Step 1: Read the markdown file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        board_id = lines[0].strip()
        list_id = lines[1].strip()
        markdown_content = ''.join(lines[2:])
    
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
        for checklist_section in card_section.find_all_next('h2'):
            checklist_title = checklist_section.get_text()
            checklist_items = [item.get_text() for item in checklist_section.find_all_next('li')]
            checklists.append({'title': checklist_title, 'items': checklist_items})
        
        cards_details.append({
            'title': card_title,
            'description': card_description,
            'checklists': checklists
        })
    
    return board_id, list_id, cards_details

# You can now use this function to parse the markdown file and get the necessary details
