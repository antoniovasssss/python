def string_repeater(text, n):
<<<<<<< HEAD
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n <= 0: 
        return ""
    
    return text * n

assert string_repeater("q", 4)
=======
    n = int(n)
    if n <= 0:
        return ""
    return text * n

print(string_repeater("q", 4))
print(string_repeater("go", 2))
print(string_repeater("tac", 3))
>>>>>>> aba3510ea976801f8145bd5ac39ba25b6fc04bbb
