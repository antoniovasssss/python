def case_change(text: str, make_upper: bool) -> str:
    # Receive a string in text and a boolean in make_upper
    # If make_upper is True return the uppercase version of text
    if make_upper:
        return text.upper()
    # If make_upper is False return the lowercase version of text
    return text.lower()

# Simple checks
print(case_change("Super", True))     # SUPER
print(case_change("Super", False))    # super
print(case_change("AmBourine", True)) # AMBOURINE
print(case_change("AmBourine", False))# tambourine