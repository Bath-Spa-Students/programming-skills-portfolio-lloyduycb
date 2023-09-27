# Unlike Ex4, one of the items in the array is replaced.

guests = ["Shah Rukh Khan", "Amir Khan", "Salman Khan"]
greeting = ", You are invited for a dinner here at 6pm. Hope to see you there!"

print(guests[0], "Cannot make it to the party")

guests = ["Adolf Hitler", "Amir Khan", "Salman Khan"]

for guest in guests: 
    print("Dear Mr.", guest, greeting)
