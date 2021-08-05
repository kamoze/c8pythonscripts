#variables here
userReply = input("Do you need to ship a package? (Type yes or no) ")
#Conditional starts here
if userReply == "yes":
  print("We can help you ship that package!")
else:
  print("Please come back when you do need to  ship a package. Thank you.")

# Second Conditional
#variables here
userReply = input("Would you like to buy stamps, an envelope, or make a copy? (Type stamps, envelope, or copy)")
#conditional statement starts here
if userReply == "stamps":
    print("We have plenty of stamp designs to  choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Type a number)")
    print("Here" + " are " + str(copies) + " copies")
else:
    print("Thank you, please come again. We cannot help you")