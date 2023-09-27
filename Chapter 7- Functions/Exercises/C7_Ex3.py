# This program uses the function make_shirt()

def make_shirt(size, text):
    print("This shirt is size: " + size + " and '" + text + "' is printed on it.")

make_shirt("XXXXL", "Valorant.") # Calls the function.in positional order

make_shirt(text="BTS", size="XS") # Calls the function in keyword argument.