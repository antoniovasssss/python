def longer(a: str, b: str) -> str:
    len_a = len(a)
    len_b = len(b)
    if len_a >= len_b:
        return a
    return b

# run examples only when this file is executed directly
if __name__ == "__main__":
    # expect piranha
    print(longer("drum", "piranha"))
    # expect basket
    print(longer("basket", "fork"))
    # expect sustainable
    print(longer("flannel", "sustainable"))
    # expect disrupt
    print(longer("disrupt", "ability"))
    # expect bird
    print(longer("bird", "shoe"))