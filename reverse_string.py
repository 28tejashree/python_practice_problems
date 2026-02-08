# Reverse String
# I'll take string as input and return a reversed string as result
# I'll loop each character of string and build the result in reverse order.
def reverse_str(text):
    result = ""
    for ch in text:
        result = ch + result
    return result

output = reverse_str("Hello")
print(output)

print(reverse_str("madam"))
print(reverse_str(""))
