def one_to_four():
    # range starts at 1 and stops before 5 so it yields 1 2 3 4
    for n in range(1, 5):
    # print the current number
        print(n)

# run the function only when this file is executed directly
if __name__ == "__main__":
    # call the function to produce the output
    one_to_four()