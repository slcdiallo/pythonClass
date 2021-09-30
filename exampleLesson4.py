##### MODULE OS

# open(filename, mode) "r" is for reading, "w" for writing
# with block guarantees file is closed
# open expects file to be in cwd, otherwise you need to specify path
#with open("exdata.txt","r") as infile:
    #s = infile.read()  # reads the entire file as 1 string #with "with" dont need to close
#with open("output.txt","w") as outfile:
    #outfile.write("this is a test\n"); # write only does strings
    #outfile.write("%d\n" %40) # any formatting must be in the string

#StringIO works just like an output file but output is to a string.
#Helpful when the same output goes to different places,
#say screen and file. In Python, to create an object,
#you do not use any special type of operator like new.
#The class name followed by () will create a new object.
#So output = io.StringIO() creates a new object and names it output.
#The io. isneeded because it resides in the io module.

#import io
#output = io.StringIO()# creates a string IO object
#output.write("this a test\n")
#print(output.getvalue()) # getvalue returns the string output


##### MORE LOOPS

#g=(1,2,3)   # g is a tuple, uses parentheses/any kind of info can be in tuple/you cant change them
#for x in g: # loop to print all elements in g
    #print(x)
    #print(x,end="") #for results in all same line
#g=(1,2,3)
#print(g[0])   #means print the first element
#for x in g:
    #print(x)

#h=[4,5,6,7,"abc"]      # h is a list, uses []
#print(h[4])
#for x in h:            # loop to print all elements in h
    #print(x)

#s="abcdefg" # s is an str
#for x in s: # loop to print the chars in s
    #print(x,end="")         #end="" for results in all the same line
    #print(x)


##### RANGE

#for x in range(5): # think of range(5) as the sequence 0..4
    #print (x) # will print 0 1 2 3 4 (separate lines)
#g=(5,6,7)
#for x in range(len(g)): # len returns number of elements in g
    #print(x,g[x]) # prints elements with location OF EACH


##### WHILE LOOPS

#x=0
#while x < 5:           # prints 0 1 2 3 4
    #print(x)
    #x+=1

#s = input("Enter a number")
#while len(s)>0:         # terminates when you enter a blank line
    #print(s)
    #s = input("Enter another number")

##### PROGRAM 4 - EXAMPLE

while True:
   s=input("Enter another integer")
   if len(s)==0: break       # break: breakout of the current loop
   width=int(s)
   if width>=4 and width<=9:
       for j in range(width):
           print("*")
   elif width>=10 and width<=15:
       for j in range(width-1):    #use -1 to get equal characters for each side
           print("*")
       for j in range(width):
           print("* ", end="")
       print()
# for the Excercise elif for the inner loops
       


