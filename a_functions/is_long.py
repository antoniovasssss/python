def is_long(text):
    # get the number of characters in the input string
    length = len(text)
        # return True if length is more than 5 characters
    return length > 5

if __name__ == "__main__":
    print(is_long("pie"))           # False
    print(is_long("kite"))          # False
    print(is_long("kitty"))         # False
    print(is_long("telescope"))     # True
    print(is_long("thermometer"))   # True
    print(is_long("restaurant"))    # True