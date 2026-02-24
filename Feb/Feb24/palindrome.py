def palindrome (s):
    r = s[::-1]
    if s == r:
        return True
    else:
        return False
word = "madam"
print (palindrome(word))

