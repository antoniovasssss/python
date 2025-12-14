def funny_sound(a: str, b: str) -> str:
    #"""Return first three chars of a then first three chars of b."""
    return a[:3] + b[:3]  # slice first three of a then b then join

if __name__ == "__main__":
    # simple checks
    print(funny_sound("tiger", "spoon"))     # tigspo
    print(funny_sound("computer", "phone"))  # compho
    print(funny_sound("skate", "bottle"))    # skabot
    print(funny_sound("frog", "ashtray"))    # froash

