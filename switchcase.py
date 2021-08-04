# Switcher for implementing switch case options
def employee_details(ID):
    switcher = {
        "1004": "Employee Name: MD. Mehrab",
        "1009": "Employee Name: Mita Rahman",  
        "1010": "Employee Name: Sakib Al Hasan",
    }
    '''The first argument will be returned if the match found and
        nothing will be returned if no match found'''
    return switcher.get(ID, "nothing")

# Take the employee ID
ID = input("Enter the employee ID: ")
# Print the output
print(employee_details(ID))