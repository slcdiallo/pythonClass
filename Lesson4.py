#Assignment 4
#Author: Saliou Diallo

#Program 4 - Simple Ascii Drawing
#For this program, ask the user to enter an integer.
#The program will then draw a shapebased on the integer:
    #a vertical line for 4-9, an L for 10-15,
    #a horizontal line for 16-20 otherwise it says invalid input.
#The program will continue running until there is no input.

while True:
   s=input("Enter another integer")
   if len(s)==0: break       
   width=int(s)
   if width>=4 and width<=9:
       for j in range(width):
           print("*")
   elif width>=10 and width<=15:
       for j in range(width-1):    #used -1 to get equal characters for each side
           print("*")
       for j in range(width):
           print("* ", end="")
   elif width>=16 and width<=20:
       for j in range(width):
           print("* ", end="")
   else:
      print("Invalid input")
      print()

