# This program modifies the array using pop and del

guests = ["Adolf Hitler", "Amir Khan", "Salman Khan"]

for guest in guests: 
    print("Dear Mr.", guest, "Apologies for the late message; I am only able to invite 2 people for dinner.")

guests.pop(0) # pop is used to remove the first element
for guest in guests:
    print("Dear Mr.", guest, "You are still invited to the dinner at 6pm.") 

del guests[0]
del guests[0] # The last element becomes 0

print(guests)