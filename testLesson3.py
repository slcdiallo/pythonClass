import os

infile = open("data3.txt","r")

# let's set the variables that we're going to use
sum = 0.0
len = 0
hi = 0
low = 0

# let's process the file
for s in infile:
  s1 = s.split()
  x = float(s1[0])
  y = float(s1[1])
  print ("Number of items: %5d     Total price for the order: %10.2f" % (y,x*y))

  sum += x*y
  len += 1
  if (sum > hi): hi = sum
  if (low == 0 or sum < low): low = sum

print ("Avg", sum/len, "Lowest", low, "Highest", hi)
