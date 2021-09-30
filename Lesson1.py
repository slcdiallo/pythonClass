#Saliou Diallo
#Write a module that first asks the user to enter 2 integers and then print the sum, difference,
#product, quotient, integer quotient, and modulus of the 2 numbers. Then ask the user to enter 2 real
#numbers. Print the sum, difference, product, quotient, integer quotient, and modulus using the %
#operator. Specify the width and number of digits after the decimal and be sure to specify an adequate
#width. The video demonstrates some of the above in the Python IDLE.

print('Enter an integer')           #ask to enter 1 integer
x=input()
y=int(x)                            #int is to convert to integer
print('Enter another integer')      #ask to enter another integer
z=input()
w=int(z)
print('Sum:',y+w,'Difference:',y-w, 'Product:', y*w, 'Quotient:',y/w,'Integer Quotient:',y//w,'Modulus:',y%w)
#Modulus is remainder; what is left over after you divide
s=input('Enter 2 real numbers').split()
# split() gives a list of strings
a=float(s[0])                       #float is to convert to a real number
b=float(s[1])
print('Sum %5.2f Difference %5.2f Quotient %5.2f IntegerQuotient %5.3f Modulus %5.3f' % (a+b, a-b, a/b, a//b, a%b))
# % operator is used for formatting
# when you format you have to have a format string
# after formatting you have to have a tuple
# a tuple is one or more values in parenthesis seperated by a comma (1,2)



