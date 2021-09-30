from Mod2 import guiInput,guiOutput

#import os                   # os stand for operating system
#print(__file__)             # complete path of the file being executed in the shell
#print(os.getcwd())         # cwd current working directory: The folder where the shell is running the program

#import os  
#infile = open("data.txt","r")       # infile is just a name # r is for read # w is for write
#s = infile.read()                  # read will read everything in the file, it returns a string of what is in the file
#infile.close()
#print(s)                           # '\n' "\n" looks exactly what is in the file

#import os  
#infile = open("data.txt","r")
#for s in infile:       # a for loop starts with the word for # automatically does a readline # : is a block it automatically indent 
    #print(s,end="")
#infile.close()

#import os  
#infile = open("data.txt","r")
#for s in infile:
    #s2 = s.split() # s2 is another variable # split breaks it down 
    #x = float(s2[0])
    #y = float(s2[1])
    #print (s ,x*y)  # have to convert in order to do calculations
#infile.close()

#import os  
#infile = open("data.txt","r")
#avg=0.0     #wanna make sure it is float
#len=0       #wanna make sure it is int       
#for s in infile:
    #s2 = s.split()
    #x = float(s2[0])
    #print (x)
    #avg += x            # += means add to # add x to avg # so you are adding all the first numbers 
    #len += 1            # add 1 to len=count of numbers
#print ("Avg", avg/len)  # total of 1st numbers / count
#infile.close()
    
import os
infile = open("data3.txt","r")
avg=0.0     
len=0
hi=0
for s in infile:
    s2 = s.split()
    x = float(s2[0])
    print (x)
    avg += x           
    len += 1
    if x>hi : hi=x                  # when doing highest and lowest you have to use an if
print ("Avg", avg/len, "Highest", hi)
#output to a file is almost as easy as writing to the screen
outfile=open("output.txt","w")       # w open for writing #automatically create output.txt
outfile.write("Avg %f Highest %d" % (avg/len, hi)) #it would write in the output.txt the results
outfile.close()
infile.close()
