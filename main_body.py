import util as util
import search_users as u
import search_tickets as t
import search_organizations as o

# Shows the main menu. Options are given to be selected accordingly.
def mainBody(users, tickets, orgs):
    print("\nSelect 1) Users or 2) Tickets or 3) Organizations : ")
    res2 = input()

    if util.getVariableValue(res2) == 1: # Searching the users
        usrSearchTerm = input("Enter search term : ")
        util.checkQuitCommand(usrSearchTerm)
        usrSearchVal = input("Enter search value : ")
        util.checkQuitCommand(usrSearchVal)
        fUsers = u.searchUsers(users, tickets, orgs, usrSearchTerm, usrSearchVal)
        if (len(fUsers) < 1):
            print("Searching users for", usrSearchTerm, " with a value of", usrSearchVal, " \nNo results found")
        util.printOutput(fUsers)

    elif util.getVariableValue(res2) == 2: # Searching the Tickets
        tktSearchTerm = input("Enter search term : ")
        util.checkQuitCommand(tktSearchTerm)
        tktSearchVal = input("Enter search value : ")
        util.checkQuitCommand(tktSearchVal)
        finalTickets = t.searchTickets(users, tickets, orgs, tktSearchTerm, tktSearchVal)
        if (len(finalTickets) < 1):
            print("Searching tickets for", tktSearchTerm, " with a value of", tktSearchVal, " \nNo results found")
        util.printOutput(finalTickets)

    elif util.getVariableValue(res2) == 3: # Searching the organizations
        orgSearchTerm = input("Enter search term : ")
        util.checkQuitCommand(orgSearchTerm)
        orgSearchVal = input("Enter search value : ")
        util.checkQuitCommand(orgSearchVal)
        finalOrgs = o.searchOrganizations(users, tickets, orgs, orgSearchTerm, orgSearchVal)
        if (len(finalOrgs) < 1):
            print("Searching organizations for", orgSearchTerm, " with a value of", orgSearchVal, " \nNo results found")
        util.printOutputOrgs(finalOrgs)

    else:
        util.checkQuitCommand(res2)
        print("Incorrect input. Please enter a correct number!")

    mainBody(users, tickets, orgs)
