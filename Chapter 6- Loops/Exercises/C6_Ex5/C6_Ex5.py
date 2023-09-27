# This program uses while loop to remove all repeated instances.

sandwich_orders = ['pastrami', 'turkey', 'pastrami', 'ham', 'pastrami', 'roast beef', 'club']

finished_sandwiches = []

print("Sorry, we've run out of pastrami!")

while 'pastrami' in sandwich_orders: # removes all instances of 'pastrami'
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Remove the first order from the list
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)