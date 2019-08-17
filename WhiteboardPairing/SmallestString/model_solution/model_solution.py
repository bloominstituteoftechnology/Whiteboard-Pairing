def parse_number(string, index):
    number_length = 0
    number_value = ''
    
    while index < len(string) and string[index].isdigit():
        number_length += 1
        number_value += string[index] 
        index += 1

    return (int(number_value), number_length)


def shortest_string(str1, str2):
    s1 = 0
    s2 = 0
    len1 = len(str1) - 1
    len2 = len(str2) - 1

    while s1 <= len1 and s2 <= len2:
        if str1[s1].isalpha() and str2[s2].isalpha():
            if str1[s1] == str2[s2]:
                s1 += 1
                s2 += 1
            else:
                return str1 if str1[s1] < str2[s2] else str2
        else:
            if str1[s1].isdigit() and str2[s2].isdigit():
                n1, l1 = parse_number(str1, s1)
                n2, l2 = parse_number(str2, s2)
                
                if n1 != n2:
                    return str1 if n1 < n2 else str2
                else:
                    s1 += l1
                    s2 += l2
            else:
                return str1 if str1[s1] < str2[s2] else str2
            
    return str1 if len1 < len2 else str2


# Tests
print(shortest_string("a", "b"))              # should print "a"
print(shortest_string("a1", "a2"))            # should print "a1"
print(shortest_string("a10", "a2"))           # should print "a2"
print(shortest_string("abcd123", "abc123"))   # should print "abc123"
print(shortest_string("abc", "abcd"))         # should print "abc"
print(shortest_string("abc123a", "abc123b"))  # should print "abc123a"
print(shortest_string("9876", "987"))         # should print "987"
print(shortest_string("6a", "6b"))            # should print "6a"
