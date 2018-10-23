# is it tuesday
# Michael Kidd

import datetime

today = datetime.datetime.today()
dayOfWeek = today.weekday()

if dayOfWeek == 1:
    print("Its Tuesday!")
elif dayOfWeek == 0: 
    print("it is not tuesday!")
    print("It will be tuesday tomorrow!")
else:
    print("It is not Tuesday")

print("Thank you for checking if its tuesday!")
