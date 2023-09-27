# This code creates a dictionary with different elements representing a pet; used a for loop to iterate through the list.

pets = [
    {'kind': 'Goldfish', 'owner': 'Jacob'},
    {'kind': 'Cat', 'owner': 'Francis'},
    {'kind': 'Tiger', 'owner': 'Debby'},
    {'kind': 'Dog', 'owner': 'Isaiah'}
]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']} \n")  # Add a blank line to separate each pet's information using \n