# This program makes sandwiches based on the list; prints each sandwich and gets added to an empty list.

sandwich_orders = ['tuna', 'turkey', 'veggie', 'ham', 'chicken'] # initial orders for sandwiches

finished_sandwiches = [] # empty list to store finished sandwiches

while sandwich_orders: # in a while loop as long as there are sandwiches in the initial order
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())
