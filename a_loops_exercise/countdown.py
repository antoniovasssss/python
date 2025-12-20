def countdown(start: int) -> None:
    # Ensure the input is an integer and positive
    if not isinstance(start, int) or start < 1:
        # Inform the user and return early if the input is invalid
        print("start must be a positive integer")
        return 
    # Use a while loop to print from start down to 1
    current = start # set the loop counter to the starting value
    while current >= 1: # continue until we reach 1
        print(current) # print the current number
        current -= 1 # decrease the counter by 1 each iteration

# Optional demo when running this file directly        
if __name__ == "__main__":
    # Example run that prints 5 4 3 2 1 on separate lines
    countdown(5)