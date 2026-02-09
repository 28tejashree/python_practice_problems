#Count vowels in a string
# I'll loop through a string and check each char
# If char is vowel, I'll increase count

def count_vowels(text):
    count = 0
    vowels = "aeiou"
    text = text.lower()
    
    for ch in text:
        if ch in vowels:
            count = count + 1
    return count
print(count_vowels("Animal"))
