import sys
import util as util

# Search the users and displays the output
def searchUsers(users, tickets, orgs, usrSearchTerm, usrSearchVal):
    finalUsers = {}
    for user in users:
        try:
            if user.get(usrSearchTerm) == util.getVariableValue(usrSearchVal):
                # print(json.dumps(user, indent=2))
                if ("_id" in user):
                    finalUsers["_id"] = user['_id']
                if ("external_id" in user):
                    finalUsers["external_id"] = user['external_id']
                if ("name" in user):
                    finalUsers["name"] = user['name']
                if ("alias" in user):
                    finalUsers["alias"] = user['alias']
                if ("created_at" in user):
                    finalUsers["created_at"] = user['created_at']
                if ("active" in user):
                    finalUsers["active"] = user['active']
                if ('verified' in user):
                    finalUsers["verified"] = user['verified']
                if ("shared" in user):
                    finalUsers["shared"] = user['shared']
                if ("locale" in user):
                    finalUsers["locale"] = user['locale']
                if ("timezone" in user):
                    finalUsers["timezone"] = user['timezone']
                if ("last_login_at" in user):
                    finalUsers["last_login_at"] = user['last_login_at']
                if ("email" in user):
                    finalUsers["email"] = user['email']
                if ("phone" in user):
                    finalUsers["phone"] = user['phone']
                if ("signature" in user):
                    finalUsers["signature"] = user['signature']
                if ("organization_id" in user):
                    finalUsers["organization_id"] = user['organization_id']
                if ("tags" in user):
                    finalUsers["tags"] = user['tags']
                if ("suspended" in user):
                    finalUsers["suspended"] = user['suspended']
                if ("role" in user):
                    finalUsers["role"] = user['role']

                i = 0
                for tic in tickets:
                    if (tic["submitter_id"] == user["_id"]):
                        ticketLabel = "ticket_",i
                        finalUsers[ticketLabel] = tic['subject']
                        # print("ticket_",i,'             ', tic['subject'])
                        i = i + 1
                        for org in orgs:
                            if (tic["organization_id"] == org["_id"]):
                                finalUsers["organization_name"] = org['name']
                                # print("organization_name", '     ', org['name'])
                break

        except Exception as e:
            print(e)
            sys.exit()

    return finalUsers
