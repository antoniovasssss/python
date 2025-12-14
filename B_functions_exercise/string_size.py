def string_size(s: str) -> str:
    n = len(s)
    if n < 5:
        return "small"
    if n == 5:
        return "medium"
    return "large"

# Quick checks
print(string_size("cat"))                # small
print(string_size("bells"))              # medium
print(string_size("ready"))              # medium
print(string_size("shirt"))              # medium
print(string_size("shallow"))            # large
print(string_size("intelligence"))       # large