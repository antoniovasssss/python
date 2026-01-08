def get_average_age(people):
    # initializes a variable to track the total age
    total_age = 0
    # loops through each person dictionary in the list
    for person in people:
        # add each person's age to the total
        total_age += person["age"]
    # divides the total by the number of people to get the average
    return total_age / len(people)



peeps = [
    {"name":"Lovelace","age":36,"born":"London, UK" },
    {"name":"Kleene","age":85,"born":"Connecticut, US" },
    {"name":"Turing","age":41,"born":"London, UK" },
    {"name":"Hopper","age":85,"born":"New York, US" },
]

print(get_average_age(peeps))

people = [
    {"name":"Orwell","age":46,"born":"Bihar, India" },
    {"name":"Bradbury","age":91,"born":"California, US" },
    {"name":"Huxley","age":69,"born":"California, US" },
]

print(get_average_age(people))

