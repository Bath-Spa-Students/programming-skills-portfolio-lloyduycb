# This program uses strips in order to remove whitespace

name = "\n      Lylod       \t"

x = name.lstrip() # lstrip() removes the left side
print(x, "so nice")

y = x.rstrip()
print(y, "is bad boy") # rstrip() removes the right side

name = name.strip() # strip() removes both sides
print(name, ".")