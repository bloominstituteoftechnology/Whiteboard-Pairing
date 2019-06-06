// js doesn't have an exact equivalent of Python's 
// `isdigit` method, but we can implement one ourselves
// using a simple regex
function isDigit(str) {
    return str.match(/[0-9]/i);
}

// Similarly, we'll make a helper function using a regex
// to determine if a character is a (lowercase) letter
function isAlpha(str) {
    return str.match(/[a-z]/i);
}

function parseNumber(string, index) {
    let numberLength = 0;
    let numberValue = '';

    while (index < string.length && isDigit(string[index])) {
        numberLength++;
        numberValue += string[index];
        index++;
    }
    
    // use `parseInt` to parse the string `numberValue` to
    // an integer type in base 10 
    return [parseInt(numberValue, 10), numberLength];
}

function shortestString(str1, str2) {
    let s1 = 0;
    let s2 = 0;
    const len1 = str1.length - 1;
    const len2 = str2.length - 1;

    while (s1 <= len1 && s2 <= len2) {
        if (isAlpha(str1[s1]) && isAlpha(str2[s2])) {
            if (str1[s1] === str2[s2]) {
                s1++;
                s2++;
            } else {
                return str1[s1] < str2[s2] ? str1 : str2;
            }
        } else {
            if (isDigit(str1[s1]) && isDigit(str2[s2])) {
                let [n1, l1] = parseNumber(str1, s1);
                let [n2, l2] = parseNumber(str2, s2);

                if (n1 !== n2) {
                    return n1 < n2 ? str1 : str2;
                } else {
                    s1 += l1;
                    s2 += l2;
                }
            } else {
                return str1[s1] < str2[s2] ? str1 : str2;
            }
        }
    }

    return len1 < len2 ? str1 : str2;
}


// Tests
console.log(shortestString("a", "b"));              // should print "a"
console.log(shortestString("a1", "a2"));            // should print "a1"
console.log(shortestString("a10", "a2"));           // should print "a2"
console.log(shortestString("abcd123", "abc123"));   // should print "abc123"
console.log(shortestString("abc", "abcd"));         // should print "abc"
console.log(shortestString("abc123a", "abc123b"));  // should print "abc123a"
console.log(shortestString("9876", "987"));         // should print "987"
console.log(shortestString("6a", "6b"));            // should print "6a"
