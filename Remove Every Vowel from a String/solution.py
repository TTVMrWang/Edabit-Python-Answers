def remove_vowels(txt):
    return ''.join(char for char in txt if not char in "aeiouAEIOU")
