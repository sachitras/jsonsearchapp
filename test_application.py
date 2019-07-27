import json
import unittest
import search_users as u
import search_tickets as t
import search_organizations as o

class TestApp(unittest.TestCase):

    # Open the JSON files.
    file_users = open('JSON_OBJ/test/users.json')
    file_organizations = open('JSON_OBJ/test/organizations.json')
    file_tickets = open('JSON_OBJ/test/tickets.json')

    users = json.load(file_users)
    tickets = json.load(file_tickets)
    orgs = json.load(file_organizations)

    # Test for a valid scenario (where the given user exsists in the file)
    def test_user_search_1(self):
        user = u.searchUsers(self.users, self.tickets, self.orgs, "_id", "1")
        self.assertIsNotNone(user)
        found = False
        if ("_id" in user):
            found = True
        self.assertTrue(found)
        self.assertEqual(user["phone"], "8335-422-718")
        self.assertEqual(user["shared"], False)
        self.assertEqual(user["timezone"], "Sri Lanka")
        self.assertEqual(user["active"], True)
        self.assertEqual(user["role"], "admin")
        self.assertEqual(user["organization_name"], "Qualitern")

    # Test for an invalid scenario (where the given user does not exist in the file)
    def test_user_search_2(self):
        user = u.searchUsers(self.users, self.tickets, self.orgs, "_id", "344")
        found = False
        if ("_id" in user):
            found = True
        self.assertFalse(found)

    # Test for a valid ticket.
    def test_ticket_search_1(self):
        ticket = t.searchTickets(self.users, self.tickets, self.orgs, "external_id", "74e795dd-fb0d-48aa-9c83-f90016ca8243")
        self.assertIsNotNone(ticket)
        found = False
        if ("_id" in ticket):
            found = True
        self.assertTrue(found)
        self.assertEqual(ticket["type"], "task")
        self.assertEqual(ticket["subject"], "A Drama in Australia")
        self.assertEqual(ticket["status"], "solved")
        self.assertEqual(ticket["organization"], "Speedbolt")

    # Test for an invalid ticket.
    def test_ticket_search_2(self):
        ticket = t.searchTickets(self.users, self.tickets, self.orgs, "external_id", "74e795dd-fb0d-48aa-9c83-f916ca8243")
        found = False
        if ("_id" in ticket):
            found = True
        self.assertFalse(found)

    # Test for a valid organization
    def test_organization_search_1(self):
        org = o.searchOrganizations(self.users, self.tickets, self.orgs, "_id", "105")
        self.assertIsNotNone(org)
        found = False
        if ("_id" in org):
            found = True
        self.assertTrue(found)
        self.assertEqual(org["Organization name"], "Koffee")

    # Test for invalid organization
    def test_organization_search_2(self):
        org = o.searchOrganizations(self.users, self.tickets, self.orgs, "_id", "343")
        found = False
        if ("_id" in org):
            found = True
        self.assertFalse(found)

if __name__ == '__main__':
    unittest.main()
