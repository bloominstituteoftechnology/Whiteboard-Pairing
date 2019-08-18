# Start a formula that takes in the string of variables.
# Iterate over the characters in the string.
# Keep track of each of the types of characters, + for open, - for close.
# Check the values for each of the characters to see if they are 0 or not.
# If all are zero, return true.
# If not zero, return false.
# return character_counter + character_counter + character_counter == 0


def balancedBrackets(string):
    bracket_counter = 0
    braces_counter = 0
    parantheses_counter = 0
    for character in string:
        if character == "[":
            bracket_counter += 1
        if character == "{":
            braces_counter += 1
        if character == "(":
            parantheses_counter += 1
        if character == "]":
            bracket_counter -= 1
        if character == "}":
            braces_counter -= 1
        if character == ")":
            parantheses_counter -= 1

    return bracket_counter + braces_counter + parantheses_counter == 0


print(balancedBrackets('{}[]()'))        # should print True
print(balancedBrackets('{(([]))}'))      # should print True
print(balancedBrackets('{ [ ] ( ) }'))   # should print True
print(balancedBrackets('{ [ ( ] ) }'))   # should print False
print(balancedBrackets('('))             # should print False
print(balancedBrackets('{[}'))           # should print False
