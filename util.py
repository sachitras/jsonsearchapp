import sys

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

# Printing out the search results
def printOutput(values):
    for key, value in values.items():
        print(str(key).ljust(30), value)
