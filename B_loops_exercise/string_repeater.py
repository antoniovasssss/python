def string_repeater(text, n):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n <= 0: 
        return ""
    
    return text * n

assert string_repeater("q", 4)