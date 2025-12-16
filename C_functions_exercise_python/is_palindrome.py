def is_palindrome(text):
    # Build a lowercase string with only letters and digits
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    # Compare the cleaned string to its reverse
    return cleaned == cleaned[::-1]

print(is_palindrome("level"))       # True
print(is_palindrome("Race car"))    # True
print(is_palindrome("python"))      # False
print(is_palindrome("No lemon no melon"))  # True