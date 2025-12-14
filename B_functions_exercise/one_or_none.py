def one_or_none(a: bool, b:
    bool) -> bool:
    # a != b is True only when exactly one is True
    # if both are True it returns False
    # if both are False it returns False
    return a != b

if __name__ == "__main__":
    # sample checks from the prompt
    print(one_or_none(False, False))  # False
    print(one_or_none(True, False))   # True
    print(one_or_none(False, True))   # True
    print(one_or_none(True, True))    # False