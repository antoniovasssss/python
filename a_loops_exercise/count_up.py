def count_up(max_num):
    # Define a function named count_up that takes one parameter called max_num

    if not isinstance(max_num, int):
     # Guard clause to ensure the argument is an integer

        raise TypeError("max_num must be an int")
    
    if max_num < 1:
     # If max_num is less than 1 there is nothing to count
        return
    
    for i in range(1, max_num + 1):
    # Use a for loop to iterate over numbers starting at 1 and ending at max_num
        print(i)
        # Print the current number

if __name__ == "__main__":
    # Only runs when you execute this file directly
    count_up(5)
    count_up(3)