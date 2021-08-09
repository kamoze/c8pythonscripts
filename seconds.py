#!/usr/bin/python3
# Python Program to Convert seconds
# into hours, minutes and seconds
# This is a comment - not processed
  
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
      
# Driver program
n = int(input("Input the seconds:"))
print(convert(n))

ca = 10
ca = ca += int(5)

print(ca)



