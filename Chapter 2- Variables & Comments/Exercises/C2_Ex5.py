# This program shows the uses of arithmetics

money = 50
cost = 6
quantity = round(money/cost) # / is used for division; round() is a function that rounds up the value
change = money-(cost*quantity)

print("She can buy", quantity, "of her favourite USB Sticks and have a change of £", change) 