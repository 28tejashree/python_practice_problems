# Count frequency of characters in a string
# I'll use dictionary to store character count in string
# I'll loop through string if found repeated charcter I'll update count otherwise I'll keep as 1

def count_char_frequency(text):
    freq = {}
    text = text.lower()
    for ch in text:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1
    return freq
print(count_char_frequency("Tejashreet0012333"))
