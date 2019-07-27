import util as util

# Search the tickets and displays the output
def searchTickets(users, tickets, orgs, tktSearchTerm, tktSearchVal):
    finalTickets = {}
    for ticket in tickets:
        try:
            if ticket.get(tktSearchTerm) == util.getVariableValue(tktSearchVal):

                if ("_id" in ticket):
                    finalTickets["_id"] = ticket['_id']
                if ("type" in ticket):
                    finalTickets["type"] = ticket['type']
                if ("subject" in ticket):
                    finalTickets["subject"] = ticket['subject']
                if  ("description" in ticket):
                    finalTickets["description"] = ticket['description']
                if ("status" in ticket):
                    finalTickets["status"] = ticket['status']
                if ("tags" in ticket):
                    finalTickets["tags"] = ticket['tags']

                for usrAs in users:
                    if("assignee_id" in ticket):
                        if (usrAs["_id"] == ticket["assignee_id"]):
                            finalTickets["assignee"] = usrAs['name']
                            break
                for usrSub in users:
                    if("submitter_id" in ticket):
                        if (usrSub["_id"] == ticket["submitter_id"]):
                            finalTickets["submitter"] = usrSub['name']
                            break
                for org in orgs:
                    if("organization_id" in ticket):
                        if (ticket["organization_id"] == org["_id"]):
                            finalTickets["organization"] = org['name']
                            break
        except:
            print("Searching tickets for", tktSearchTerm, " with a value of", tktSearchVal, " \nNo results found")

    return finalTickets
