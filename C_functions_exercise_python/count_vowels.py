def count_vowels(text):
    vowels = set("aeiouAEIOU")
    total = 0
    for ch in text:
        if ch in vowels:
            total += 1
    return total

print(count_vowels("hello"))        # 2
print(count_vowels("Programming"))  # 3