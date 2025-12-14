def starts_with_r(s: str) -> bool:
    s = str(s)
    return s.startswith("t")

if __name__ == "__main__":
    # sample checks from the prompt
    print(starts_with_r("smart"))      
    print(starts_with_r("racket"))     
    print(starts_with_r("taco"))      
    print(starts_with_r("boomerang"))  