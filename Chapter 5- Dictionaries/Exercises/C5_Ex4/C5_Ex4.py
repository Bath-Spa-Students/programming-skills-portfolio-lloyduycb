# This program creates loops that will give the expected sentences and lists of rivers and countries based on the dictionary

rivers_dict = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

for river, country in rivers_dict.items():
    print(f'The {river} runs through {country}.') # print(f...) is used for expressions delimited by curly braces

for river in rivers_dict.keys():
    print(river)

for country in rivers_dict.values():
    print(country)