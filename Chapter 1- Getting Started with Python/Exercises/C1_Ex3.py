# This program shows the current date and time

from datetime import datetime

now = datetime.now() # shows raw time
dateTimeString = now.strftime("%d/%m/%Y %H:%M:%S") # formats the date and time into a string
print("Today", dateTimeString) # The strings are concatenated with a comma.