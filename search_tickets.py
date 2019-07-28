import util as util

# Search the tickets and displays the output
def searchTickets(users, tickets, orgs, tktSearchTerm, tktSearchVal):
    finalTickets = []
    for ticket in tickets:
        try:
            if ticket.get(tktSearchTerm) == util.getVariableValue(tktSearchVal):
                newticket = {}
                if ("_id" in ticket):
                    newticket["_id"] = ticket['_id']
                if ("type" in ticket):
                    newticket["type"] = ticket['type']
                if ("subject" in ticket):
                    newticket["subject"] = ticket['subject']
                if  ("description" in ticket):
                    newticket["description"] = ticket['description']
                if ("status" in ticket):
                    newticket["status"] = ticket['status']
                if ("tags" in ticket):
                    newticket["tags"] = ticket['tags']

                for usrAs in users:
                    if("assignee_id" in ticket):
                        if (usrAs["_id"] == ticket["assignee_id"]):
                            newticket["assignee"] = usrAs['name']
                            break
                for usrSub in users:
                    if("submitter_id" in ticket):
                        if (usrSub["_id"] == ticket["submitter_id"]):
                            newticket["submitter"] = usrSub['name']
                            break
                for org in orgs:
                    if("organization_id" in ticket):
                        if (ticket["organization_id"] == org["_id"]):
                            newticket["organization"] = org['name']
                            break
                # A line seperation between a list of tickets            
                newticket[""] = ""
                finalTickets.append(newticket)
        except:
            print("Searching tickets for", tktSearchTerm, " with a value of", tktSearchVal, " \nNo results found")

    return finalTickets
