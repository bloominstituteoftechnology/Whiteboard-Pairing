/*  
    For this problem, it's important to think about which 
    data structures to use in order to achieve the functionality
    we're looking for. Think about _why_ these particular data
    structures were used in the solution code. Could we have used
    alternative ones? What would be the resulting tradeoffs?
*/

import Foundation

func balancedBrackets(_ string: String) -> Bool {
    // Dictionary to map opening brackets to their corresponding closing bracket
    let closingBracesForOpeningBraces: [Character : Character] = [
        "(" : ")",
        "{" : "}",
        "[" : "]",
    ]
    
    func isOpeningBrace(_ b: Character) -> Bool {
        return closingBracesForOpeningBraces[b] != nil
    }
    
    func isClosingBrace(_ b: Character) -> Bool {
        return closingBracesForOpeningBraces.values.contains(b)
    }
    
    var stack = [Character]() // Stack to keep track of opening brackets
    
    for letter in string {
        if isOpeningBrace(letter) {
            stack.append(letter)
        } else if isClosingBrace(letter) {
            // Check to see if this closing brace is correct for the top opening brace on the stack
            guard let mostRecentOpener = stack.popLast(),
            letter == closingBracesForOpeningBraces[mostRecentOpener] else { 
                // Saw a closer without having seen an opener
                return false 
            }
        }
    }
    return stack.count == 0 // Return true if we're not left with any unterminated opening braces
}

print(balancedBrackets("{}[]()"));        // should print true
print(balancedBrackets("{(([]))}"));      // should print true
print(balancedBrackets("{ [ ] ( ) }"));   // should print true
print(balancedBrackets("{ [ ( ] ) }"));   // should print false
print(balancedBrackets("("));             // should print false
print(balancedBrackets("{[}"));           // should print false