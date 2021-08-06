# Your variables here

age = int(input("What is your age?: "))
sex = input("Are you Male or Female: ")

if age >= 18:
    if sex == "Male":
        print('')
        print("Hi there, you are welcome to the Calvin Klein Mens Shop")
    else:
        print('')
        print("Sorry try the next shop for the Women's Shop")
else:
    print('')
    print("You are not of age. Please come back when you are older")
