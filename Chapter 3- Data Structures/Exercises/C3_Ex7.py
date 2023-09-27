# This program shows how to sort orders using sorted() and sort()

places = ["China", "Japan", "Korea", "Thailand", "Laos"]

print(places)

print(sorted(places)) # Sorted in alphabetical order (A-Z) using sorted()

print(places)

print(sorted(places, reverse=True)) # Parameter "Reverse" is set to True

print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)