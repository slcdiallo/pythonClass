#For this program you will ask the user to enter the name of a text file.
#Each line in the file will contain two numbers, the first number is the price
#of each widget and the second line is the number of widgets in the order.
#For each line, print the number of items and the total price for the order (widgets*price).
#At the end, print the highest order, the lowest order, and the average order.
#Console output is sufficient.

import os
infile = open("data3.txt","r")
orders = []
for line in infile:
	price,count = line.split()
	price,count = [float(price),int(count)]
	print("Items: %1.2f (Total: %1.2f)" % (count,count*price))
	orders += [price*count]
	
	

print("The largest order was: ", max(orders))
print("The smallest order was: ", min(orders))
print("The average order was: ", sum(orders)/len(orders))

infile.close();
