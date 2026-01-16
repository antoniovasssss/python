def average(num1, num2):
    print("calculating...")
    return(num1 + num2) / 2

print(average(5, 10)) # returns (5 + 10) / 2 = 7.5
print(average(20, 26)) # returns (20 + 26) / 2 = 23.0
print(average(50, 100) + 2) # calculates (50 + 100) / 2 = 75, then adds 2 = 77.0

a = 21 + 3 # = 24
b = 20
n = average(a, b) # returns (24 + 20) / 2 = 22
print(average(n, 18)) # returns (22 + 18) / 2 = 21.0