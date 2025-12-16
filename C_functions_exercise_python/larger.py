def larger(a, b):
    # use a conditional expression to return a if it is greater than or equal to b
    # otherwise return b
    return a if a >= b else b

# simple checks that match the examples
print(larger(256, 400))   # 400
print(larger(31, 4))      # 31
print(larger(-6, 7))      # 7
print(larger(11.3, 11.2)) # 11.3
print(larger(-10, -3))    # -3