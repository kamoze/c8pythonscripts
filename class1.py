# Define the class
class Employee:
    name = "Mostak Mahmud"
    # Define the method
    def details(self):
        print("Post: Marketing Officer")
        print("Department: Sales")
        print("Salary: $1000")

# Create the employee object    
emp = Employee()
# Print the class variable
print("Name:",emp.name)
# Call the class method
emp.details()