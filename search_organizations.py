import util as util

# Search the organizations and displays the output
def searchOrganizations(users, tickets, orgs, orgSearchTerm, orgSearchVal):
    finalOrgs = {}
    for org in orgs:
        try:
            if org.get(orgSearchTerm) == util.getVariableValue(orgSearchVal):

                if ("_id" in org):
                    finalOrgs["_id"] = org["_id"]
                if ("name" in org):
                    finalOrgs["Organization name"] = org["name"]
                finalOrgs["Tickets"] = ""
                finalOrgs["-------"] = ""
                for tik in tickets:
                    if("organization_id" in tik):
                        if(tik["organization_id"] == org["_id"]):
                            finalOrgs["Ticket subject"] = tik['subject']
                            for usr in users:
                                if("submitter_id" in tik):
                                    if(tik["submitter_id"] == usr["_id"]):
                                        finalOrgs["User"] = usr['name']
                                        break
                            finalOrgs["-------"] = ""
        except Exception as e:
            print(e)
            print("Exception when searching organizations")

    return finalOrgs
