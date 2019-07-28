import util as util

# Search the organizations and displaying the output
def searchOrganizations(users, tickets, orgs, orgSearchTerm, orgSearchVal):
    finalOrgs = []
    for org in orgs:
        try:
            if org.get(orgSearchTerm) == util.getVariableValue(orgSearchVal):
                newOrg = {}
                if ("_id" in org):
                    newOrg["_id"] = org["_id"]
                if ("name" in org):
                    newOrg["Organization name"] = org["name"]
                newOrg["Tickets"] = ""
                newOrg["-------"] = ""
                ticketList = []
                for tik in tickets:
                    if("organization_id" in tik):
                        if(tik["organization_id"] == org["_id"]):
                            for usr in users:
                                if("submitter_id" in tik):
                                    if(tik["submitter_id"] == usr["_id"]):
                                        newTik = {}
                                        newTik["Ticket subject"] = tik["subject"]
                                        newTik["User"] = usr["name"]
                                        ticketList.append(newTik)
                                        break
                            newOrg["tickets"] = ticketList
                            newOrg["-------"] = ""
                finalOrgs.append(newOrg)
        except Exception as e:
            print(e)
            print("Exception when searching organizations")

    return finalOrgs
