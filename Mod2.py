import tkinter as tk
import tkinter.font as Font
# Program 2

def center(widget,relx,rely):
    """ places top-level window on display relative to relx,rely """
    widget.withdraw()   # Remain invisible while we fig+ure out the geometry    
    widget.update_idletasks() # Actualize geometry information    
    m_width = widget.winfo_screenwidth()
    m_height = widget.winfo_screenheight()    
    w_width = widget.winfo_reqwidth()      
    w_height = widget.winfo_reqheight()
    x = (m_width - w_width) * relx
    y =  (m_height - w_height) * rely
    widget.geometry("+%d+%d" % (x,y))    
    widget.deiconify() 
   
def guiInput(prompt,xlen=24,relx=0.4, rely=0.4,extra=0,fntName="Calibri 14"):
    """Works like input but uses Entry, based on javax.swing.JOptionPane.showInputDialog
    """
    root = tk.Tk()
    result=""
    def setResult(event=None):        
        nonlocal result
        result = t2.get()        
        root.destroy()      
    caption=tk.Label(root,text="Input",bg="black",fg="white")
    caption.pack(fill=tk.X,padx=1,pady=1)        
    body=tk.Frame(root)    
    body.pack(padx=4)
    t= tk.Label(body,text=prompt,anchor=tk.W)        
    t.pack(fill=tk.X)
    xlen=max(len(prompt),xlen)+extra
    t2 = tk.Entry(body,width=xlen,font=fntName)
    t2.pack(padx=4,fill=tk.X);
    t2.focus_set();
    t2.bind('<Return>',setResult)
    okbtn = tk.Button(body, text='Ok',command=setResult)
    okbtn.pack(ipadx=12,anchor=tk.E,pady=4)
  #  root.overrideredirect(True)
    center(root,relx,rely)
    root.focus_force()
    root.mainloop()
    return result.replace("\n","")

def guiOutput(content:str,title="Output",ex1=None,extra=0,relx=0.4, rely=0.4,fntName="Monaco"):
    """string output to a Window, based on javax.swing.JOptionPane.showMessageDialog
    """
    root=tk.Tk()                        
    tk.Label(root,text=title,bg="black",fg="white").pack(fill=tk.X,padx=1,pady=1)
    w=content if type(content) is list else content.split(sep="\n")
    
    #w=content.split(sep="\n")
    xlen=0
    fnt = Font.Font(font=fntName)    
    xw=0
    
    fntHeight=fnt.metrics()['linespace']-4;
    for i in range(len(w)):
       glen=fnt.measure(w[i])+extra
       if glen>xw:
          xw=glen
    
    body=tk.Frame(root,width=xw+40,height=len(w)*fntHeight+4)
    body.pack()
    
    for i in range(len(w)):      
      tk.Label(body,text=w[i],font=fnt,anchor=tk.W).place(x=17,y=i*fntHeight+4,width=xw+4,height=fntHeight)           
    okbtn = tk.Button(root, text='Ok',command=root.destroy)
    okbtn.pack(ipadx=12,padx=12,anchor=tk.E,pady=4)
    okbtn.focus_set()
   # root.overrideredirect(True)
    center(root,relx,rely)         
    root.wait_visibility()    
    root.focus_force()
    root.mainloop()
    
def guiGrid(content:list,title="Output",ex1=None,extra=0,relx=0.4, rely=0.4,fntName="Calibri 16"):
    """string output to a Window, based on javax.swing.JOptionPane.showMessageDialog
    """
    
    root=tk.Tk()                        
    tk.Label(root,text=title,bg="black",fg="white").pack(fill=tk.X,padx=1,pady=1)
    #w=content if type(content) is list else content.split(sep="\n")
    
    #w=content.split(sep="\n")
    xlen=0
    fnt = Font.Font(font=fntName)
    w=content
    xw=[]
    for g in range(len(w[0])):
        xw.append(0);
    fntHeight=fnt.metrics()['linespace']-4;
    clen=min(40,len(w))
    for i in range(clen):
       for g in range(len(w[i])):
           glen=fnt.measure(w[i][g])+extra
           if glen>xw[g]:
              xw[g]=glen
    xtotal=0
    for i in xw:
        xtotal+=i+4
    body=tk.Frame(root,width=xtotal+40,height=clen*fntHeight+4)
    body.pack()
    anchors=[]
    for i in range(len(w[2])):
        s=w[2][i]
        anc=tk.W
        if type(s)==str:
           pos= s.find(".")
        
           if s.isnumeric() or (pos>0 and s[:pos].isnumeric() and s[pos+1].isnumeric()):
             anc=tk.E
        else:
            anc=tk.E
        anchors.append(anc)
    
    for i in range(clen):
      pos=17
      for g in range(len(w[i])):
         s=w[i][g]
         anc = anchors[g]
         tk.Label(body,text=w[i][g],font=fnt,anchor=anc).place(x=pos,
                               y=i*fntHeight+4,width=xw[g]+4,height=fntHeight)
         pos+=xw[g]+4
    okbtn = tk.Button(root, text='Ok',command=root.destroy)
    okbtn.pack(ipadx=12,padx=12,anchor=tk.E,pady=4)
    okbtn.focus_set()
   # root.overrideredirect(True)
    center(root,relx,rely)         
    root.wait_visibility()    
    root.focus_force()
    root.mainloop()    
def test():
    s=guiInput("Enter 2 integers",relx=0.8)
    w=s.split()
    if len(w)>0:
        x= int(w[0])
        y=int(w[1])
        guiOutput( "Input:%s\nSum     %10d\nDiff    %10d\n"
                   "Product %10d\nQuotient%10d\nModulus %10d" % (s,x+y,x-y,x*y,x/y,x%y),
                     "Results",fntName="Consolas 32",relx=0.8)

    s=guiInput("Enter 2 floats")
    w=s.split()

    if len(w)>0:
        x= float(w[0])
        y= float(w[1])
        guiOutput( "Input\t%s\nSum\t%1.2f\nDiff\t%1.2f\nProduct\t%1.2f\nQuotient\t%1.2f\nModulus\t%1.2f" % (s,x+y,x-y,x*y,x/y,x%y),
                     "Results",fntName="Calibri 32",extra=40,relx=0.8)

