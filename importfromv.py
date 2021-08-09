# Import another python script
import vacations as v

# Initialize the month list
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
# Initial flag variable to print summer vacation one time
flag = 0

# Iterate the list using for loop
for month in months:
    if month == "June" or month == "July":
        if flag == 0:
            print("Now",v.vacation1)
            flag = 1
    elif month == "December":
            print("Now",v.vacation2)
    else:
        print("The current month is",month)