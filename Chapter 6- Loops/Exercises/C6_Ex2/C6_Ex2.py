# This program allows the used to type their age and get a price depending on the age of the user.

while True:
    age = input("Please enter your age (or 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break 
    
    age = int(age)  # Converts input to an integer to compare ages
    
    if age < 3: # if-elif-else statement used to determine and print ticket price.
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")