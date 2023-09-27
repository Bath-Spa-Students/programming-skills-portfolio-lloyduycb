# This program is a loop that prompts the user to enter a series of toppings until 'uit' is given.

while True: # 'while' is used to repeatedly prompt the user for input.
    topping = input("Enter a pizza topping (or 'quit' to finish): ") # input function is used to get the user's input for a pizza topping.
    
    if topping.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered
    
    print(f"You'll add {topping} to your pizza.")