def wacky_word(a: str, b: str) -> str:
    # Check inputs are long enough so the function never returns bad data
    if len(a) < 3:
        raise ValueError("first string must be at least 3 hars")
    if len(b) < 2:
        raise ValueError("second string must be at least 2 chars")
    # Take the first 3 characters of a
    first_part = a[:3]
    # Take the last 2 characters of b
    second_part = b[-2:]
    # Join the two parts and return
    return first_part + second_part


# Run quick checks only when this file is executed directly
if __name__ == "__main__":
    # Each print shows the expected result from the prompt
    print(wacky_word("very", "kindly"))     # "verly"
    print(wacky_word("forever", "sick"))    # "forck"
    print(wacky_word("cellar", "door"))     # "celor"
    print(wacky_word("bagel", "sweep"))     # "bagep"