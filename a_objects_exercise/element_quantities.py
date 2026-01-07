def element_quantities(quantities):
    # create an empty list called result
    result = []
    # loop through each key-value pair in the dictionary
    for element, quantity in quantities.items():
        # for each element, adds it to the list as many times as its quantity
        for i in range(quantity):
            result.append(element)
            # returns the final list
    return result

quantities1 = {"cat": 3, "bird": 1, "dog": 2}
print(element_quantities(quantities1))

quantities2 = {"blue": 3, "brown": 1}
print(element_quantities(quantities2))
