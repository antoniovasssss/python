def ends_with_t(s: str) -> bool:
    # make sure s is a string in case someone passes a non string
    s = str(s)
    # return True if s ends with the lowercase letter t otherwise False
    return s.endswith("t")

if __name__ == "__main__":
    print(ends_with_t("smart"))      # True
    print(ends_with_t("racket"))     # True
    print(ends_with_t("taco"))       # False
    print(ends_with_t("boomerang"))  # False