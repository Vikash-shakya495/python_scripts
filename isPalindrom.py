def isPalindrom(string):
    if len(string) <= 1:
        return string
    if(string[0] == string[-1]):
        return isPalindrom(string[1:-1])
    return False

# print(isPalindrom("racecar"))
print(isPalindrom("abcdcba"))
    