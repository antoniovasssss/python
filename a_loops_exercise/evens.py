# Write a function `evens(max_num)` that prints all positive even numbers LESS than max_num.

def evens(max_num):
     for i in range(2, max_num, 2): # this generates numbers starting from 2, up to (but not including) max_num, including by 2 each time, this gives us all positive even numbers less than max_num
          print(i) # each number is printed on its own line

evens(11)
evens(8)

