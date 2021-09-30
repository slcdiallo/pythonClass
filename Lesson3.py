#Assignment 3
#Author: Saliou Diallo

#For this program you will ask the user to enter the name of a text file. Each line in the file will
#contain two numbers, the first number is the price of each widget and the second line is the number
#of widgets in the order. For each line, print the number of items and the total price for the order
#(widgets*price) At the end, print the highest order, the lowest order, and the average order. Console
#output is sufficient.

import os

infile = open("data3.txt","r")

# let's set the variables that we're going to use
sum = 0.0
len = 0
hi = 0
lo = 0

# let's process the file
for s in infile:
  s1 = s.split()
  x = float(s1[0])
  y = float(s1[1])
  z = x*y
  print ("Number of items: %3d    Total price for the order: %5.2f" % (y,x*y))

  sum += z
  len += 1
  if (sum > hi) : hi = sum
  if (lo == 0 or sum < lo) : lo = sum

print ("Average: %5.2f Lowest: %5.2f Highest: %5.2f" % (sum/len,lo,hi))








    

    
