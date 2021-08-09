# Define a dictionary
customers = {'111': 'Mehzabin Afroze', '02457': 'Md. Ali', '02834': 'Mosarof Ahmed', '05623': 'Mila Hasan',
             '07895': 'Yaqub Ali', '05634': 'Mehboba Ferdous'}

# Append a new data

print("The customer names are:")
# Print the values of the dictionary
for customer in customers:
    print(customers[customer])

# Take customer ID as input to search
name = input("Enter customer ID:")

# Search the ID in the dictionary
for customer in customers:
    if customer == name:
        print(customers[customer])
        break
    else:
        print("Customer not in our database")
