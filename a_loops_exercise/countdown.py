def countdown(n):
    # loop has a start end and step range, the step has -1 and deducts 1 each time the for loop runs as long as its true then it exits at false
    for num in range(n, 0, -1):
        print(num)

countdown(5)