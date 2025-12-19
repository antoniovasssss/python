def evens(max_num):
    """Print all positive even numbers less than max_num."""
    # Start from 2 because 2 is the smallest positive even number
    # Stop before max_num because the requirement says less than max_num
    # Step by 2 to hit only even numbers
    for n in range(2, max_num, 2):
        print(n)
        
# Sample runs to match the prompt examples
# These lines run only when you run this file directly
if __name__ == "__main__":
    evens(11) # prints 2 4 6 8 10
    evens(8) # prints 2 4 6