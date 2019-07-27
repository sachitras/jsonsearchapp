import json
import sys
import searchFields as f
import util as u
import main_body as m

# Open the JSON files.
file_users = open('JSON_OBJ/test/users.json')
file_organizations = open('JSON_OBJ/test/organizations.json')
file_tickets = open('JSON_OBJ/test/tickets.json')

# ================= Start of the program ====================

intro = """
Type 'quit' to exit at any time. Press 'Enter' to continue

        Select search options:
            *   Press 1 to search Zendesk
            *   Press 2 to view a list of searchable fields
            *   Type 'quit' to exit
"""
res1 = input(intro)
users = json.load(file_users)
tickets = json.load(file_tickets)
orgs = json.load(file_organizations)

while True:
    if u.getVariableValue(res1) == 1: # Show the main menu
        m.mainBody(users, tickets, orgs)
    elif u.getVariableValue(res1) == 2: # Show the searchable fields
        f.displaymsg()
        res1 = input(intro)
    else:
        u.checkQuitCommand(res1)
        print("\nInvalid input. Please enter a valid input")
        res1 = input(intro)
