def greatest_population(countries):
    # initialize max_country to the first country in the list
    max_country = countries[0]
    # iterate through each country, comparing populations
    for country in countries:
        # updates max_country whenever a country with a larger population is found
        if country["population"] > max_country["population"]:
            max_country = country
    # returns the name of the country with the greatest population
    return max_country["name"]



countries1 = [
    {"name":"Cameroon","population":27744989,"gdp":38.68 },
    {"name":"Belarus","population":9477918,"gdp":59.66 },
    {"name":"Indonesia","population":267026366,"gdp":1042 },
    {"name":"Guyana","population":750204,"gdp":3.88 },
]

print(greatest_population(countries1))
# 'Indonesia'


countries2 = [
    {"name":"New Zealand","population":4925477,"gdp":204.9 },
    {"name":"Mozambique","population":30098197,"gdp":14.72 },
    {"name":"Greenland","population":57616,"gdp":2.71 },
    {"name":"Kazakhstan","population":19091949,"gdp":179.3 },
    {"name":"Burma","population":56590071,"gdp":71.21 },
]

print(greatest_population(countries2))
# 'Burma'

