def stringPalindrome(n):
    if(n == n[::-1]):
        return True
    else:
        return False
        
palindrome = stringPalindrome("racecar")   
print(palindrome)         