def average(a: float, b: float, c: float) -> float:
    # add the three inputs then divide by three to get the mean
    return (a + b + c) / 3

if __name__ == "__main__":
    # print the average of 3 10 8 which should be 7
    print(average(3, 10, 8))
    # print the average of 18 5 12 which should be 9
    print(average(18, 5, 12))
    # print the average of 6 20 40 which should be 22
    print(average(6, 20, 40))