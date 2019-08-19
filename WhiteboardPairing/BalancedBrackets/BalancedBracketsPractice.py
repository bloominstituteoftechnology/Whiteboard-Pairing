# Start a formula that takes in the string of variables.
# Iterate over the characters in the string.
# Keep track of each of the types of characters, + for open, - for close.
# Check the values for each of the characters to see if they are 0 or not.
# If all are zero, return true.
# If not zero, return false.
# return character_counter + character_counter + character_counter == 0


def balancedBrackets(string):
    array = list(string)
    bracket_counter = 0
    braces_counter = 0
    parantheses_counter = 0
    openers = {
        "(": ")"
        "{": "}"
        "[": "]"
    }
    for character in range(len(array)):
        if array[character] == "[":
            bracket_counter += 1
        if array[character] == "{":
            braces_counter += 1
        if array[character] == "(":
            parantheses_counter += 1
        if array[character] == "]":
            bracket_counter -= 1
        if array[character] == "}":
            braces_counter -= 1
        if array[character] == ")":
            parantheses_counter -= 1

    if bracket_counter + braces_counter + parantheses_counter != 0:
        return False
    for character in range(len(array)):
         if array[character] == "[":
            if array[character + 1] ==
        if array[character] == "{":
            braces_counter += 1
        if array[character] == "(":
            parantheses_counter += 1


print(balancedBrackets('{}[]()'))        # should print True
print(balancedBrackets('{(([]))}'))      # should print True
print(balancedBrackets('{ [ ] ( ) }'))   # should print True
print(balancedBrackets('{ [ ( ] ) }'))   # should print False
print(balancedBrackets('('))             # should print False
print(balancedBrackets('{[}'))           # should print False
