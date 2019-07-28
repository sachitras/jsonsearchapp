import sys
import util as util

# Search the users and displays the output
def searchUsers(users, tickets, orgs, usrSearchTerm, usrSearchVal):
    finalUsers = []
    for user in users:
        try:
            if user.get(usrSearchTerm) == util.getVariableValue(usrSearchVal):
                newUser = {}
                if ("_id" in user):
                    newUser["_id"] = user['_id']
                if ("external_id" in user):
                    newUser["external_id"] = user['external_id']
                if ("name" in user):
                    newUser["name"] = user['name']
                if ("alias" in user):
                    newUser["alias"] = user['alias']
                if ("created_at" in user):
                    newUser["created_at"] = user['created_at']
                if ("active" in user):
                    newUser["active"] = user['active']
                if ('verified' in user):
                    newUser["verified"] = user['verified']
                if ("shared" in user):
                    newUser["shared"] = user['shared']
                if ("locale" in user):
                    newUser["locale"] = user['locale']
                if ("timezone" in user):
                    newUser["timezone"] = user['timezone']
                if ("last_login_at" in user):
                    newUser["last_login_at"] = user['last_login_at']
                if ("email" in user):
                    newUser["email"] = user['email']
                if ("phone" in user):
                    newUser["phone"] = user['phone']
                if ("signature" in user):
                    newUser["signature"] = user['signature']
                if ("organization_id" in user):
                    newUser["organization_id"] = user['organization_id']
                if ("tags" in user):
                    newUser["tags"] = user['tags']
                if ("suspended" in user):
                    newUser["suspended"] = user['suspended']
                if ("role" in user):
                    newUser["role"] = user['role']

                i = 0
                for tic in tickets:
                    if (tic["submitter_id"] == user["_id"]):
                        ticketLabel = "ticket_",i
                        newUser[ticketLabel] = tic['subject']
                        i = i + 1
                        for org in orgs:
                            if (tic["organization_id"] == org["_id"]):
                                newUser["organization_name"] = org['name']
                                break
                finalUsers.append(newUser)                

        except Exception as e:
            print(e)
            sys.exit()

    return finalUsers
