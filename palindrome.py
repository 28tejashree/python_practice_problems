# Palindrome String
# I take string as input and reversed the string
# stored the output in reversed_string new vaiable
# Compare orignial string and revesed string
# if both are are equal then return true otherwise false

def is_palindrome(text):
    reversed_string = ""
    for ch in text:
        reversed_string = ch + reversed_string
    if reversed_string == text:
        return True
    else:
        return False
print(is_palindrome('madam'))
