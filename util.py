import sys
import types

# Exit the program if the user enters 'quit' command
def checkQuitCommand(command):
    if command == 'quit':
        print("Goodbye!")
        sys.exit()

# Converts the variable if it is of the type 'int',
# if not, returns the variable as it is (without casting)
def getVariableValue(variableVal):
    if variableVal.isdigit():
        return int(variableVal)
    return variableVal

# Printing out the search results for organizations
def printOutputOrgs(values):
    for i in values:
        for key, value in i.items():
            if (isinstance(value, list)):
                printOutput(value)
            else:
                print(str(key).ljust(30), value)

# Printing out the search results
def printOutput(values):
    for i in values:
        for key, value in i.items():
                print(str(key).ljust(30), value)
