def min_to_max(min_num, max_num):
    # Define a function named min_to_max that takes two arguments
    # min_num is the starting integer
    # max_num is the ending integer
    if not isinstance(min_num, int):
    # Guard clause. Ensure min_num is an integer
        raise TypeError("min_num must be an int")
    
    if not isinstance(max_num, int):
    # Guard clause. Ensure max_num is an integer
        raise TypeError("max_num must be an int")
        
    # Use range to generate integers from min_num up to and including max_num
    for i in range(min_num, max_num + 1):
    # Print the current integer
        print(i)
        
if __name__ == "__main__":
    min_to_max(5, 9)
    min_to_max(11, 13)
    min_to_max(20, 11)