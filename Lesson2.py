# Lesson 2: If Statements

from Mod2 import guiInput, guiOutput

s=guiInput("Enter three real numbers").split()
x = float(s[0])
y = float(s[1])
z = float(s[2])
if      x>0 and y>0 and z>0:
        guiOutput("Sum:%1.2f" % (x+y+z));
elif    x<0 and y>0 and z>0:
        guiOutput("Prod:%1.2f" % (y*z));
elif    x>0 and y<0 and z>0:
        guiOutput("Prod:%1.2f" % (x*z));
else:
        guiOutput("Prod:%1.2f" % (x*y));

s=guiInput("Enter two integers").split()
a = int(s[0])
b = int(s[1])
if      a<0 and b<0:
        guiOutput("Quot:%1.2f" % (a/b));
elif    a>0 and b>0:
        guiOutput("Both integers are positive");
else:   
        guiOutput("At least one integer is positive");
 
