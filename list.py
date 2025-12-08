#list examples 
nums = [10, 20, 30]
mix = ["Antonio", 24, True, 99.9]

#accessing list items(indexing and slicing)
num = [10, 20, 30, 40]
print(num[0])
print(num[-1])

#slicing
print(num[1:3])
print(num[:2])
print(num[::2])


#list manipulation
#append
nums.append(40)

#insert
nums.insert(1, 999)

#extend
nums.extend([60, 70])

#remove by value
nums.remove(20)

#pop by index
nums.pop(2)

#delete item
del nums[1]

#clear list
nums.clear()

#other useful list methods
#sorting
nums.sort()

#reverse
nums.reverse()

#count
nums.count(10)

#index
nums.index(30)


