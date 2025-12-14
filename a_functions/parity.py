def parity(n: int) -> str:
    if n % 2 == 0:
    # If the remainder is zero the number is even
        return "even"
    else:
    # Otherwise the number is odd
        return "odd"
    
if __name__ == "__main__":
    # Sample checks from the exercise
    print(parity(5))      # odd
    print(parity(7))      # odd
    print(parity(13))     # odd
    print(parity(32))     # even
    print(parity(100))    # even
    print(parity(602348)) # even