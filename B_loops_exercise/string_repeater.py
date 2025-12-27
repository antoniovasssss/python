def string_repeater(text, n):
    n = int(n)
    if n <= 0:
        return ""
    return text * n

print(string_repeater("q", 4))
print(string_repeater("go", 2))
print(string_repeater("tac", 3))
