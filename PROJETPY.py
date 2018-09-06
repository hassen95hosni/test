def fait00():
    global c00,i
    i=i+1
    if(i % 2 ==0):
        
        
        c00=1
        case_0_0.configure(image=x)
        case_0_0.configure(state=DISABLED)
    else :
        case_0_0.configure(image=y)
        case_0_0.configure(state=DISABLED)
        c00=2
    if ((c00==1 and c01==1 and c02==1)or (c10==1 and c11==1 and c12==1)or (c20==1 and c21==1 and c22==1)or (c00==1 and c10==1 and c20==1)or (c01==1 and c11==1 and c21==1)or (c02==1 and c12==1 and c22==1)or (c00==1 and c11==1 and c22==1)or (c02==1 and c11==1 and c20==1) )or ((c00==2 and c01==2 and c02==2)or (c10==2 and c11==2 and c12==2)or (c20==2 and c21==2 and c22==2)or (c00==2 and c10==2 and c20==2)or (c01==2 and c11==2 and c21==2)or (c02==2 and c12==2 and c22==2)or (c00==2 and c11==2 and c22==2)or (c02==2 and c11==2 and c20==2)) :
        resultat.configure(text="win")
        case_2_2.configure(state=DISABLED)
        case_2_1.configure(state=DISABLED)
        case_2_0.configure(state=DISABLED)
        case_1_2.configure(state=DISABLED)
        case_1_1.configure(state=DISABLED)
        case_1_0.configure(state=DISABLED)
        case_0_2.configure(state=DISABLED)
        case_0_1.configure(state=DISABLED)
        case_0_0.configure(state=DISABLED)
def fait01():
    global c01 ,i
    i=i+1
    if(i % 2 ==0):
    
        c01=1
    
        case_0_1.configure(image=x)
        case_0_1.configure(state=DISABLED)
    else :
        case_0_1.configure(image=y)
        case_0_1.configure(state=DISABLED)
        c01=2
    if ((c00==1 and c01==1 and c02==1)or (c10==1 and c11==1 and c12==1)or (c20==1 and c21==1 and c22==1)or (c00==1 and c10==1 and c20==1)or (c01==1 and c11==1 and c21==1)or (c02==1 and c12==1 and c22==1)or (c00==1 and c11==1 and c22==1)or (c02==1 and c11==1 and c20==1) )or ((c00==2 and c01==2 and c02==2)or (c10==2 and c11==2 and c12==2)or (c20==2 and c21==2 and c22==2)or (c00==2 and c10==2 and c20==2)or (c01==2 and c11==2 and c21==2)or (c02==2 and c12==2 and c22==2)or (c00==2 and c11==2 and c22==2)or (c02==2 and c11==2 and c20==2)) :
        resultat.configure(text="win")
        case_2_2.configure(state=DISABLED)
        case_2_1.configure(state=DISABLED)
        case_2_0.configure(state=DISABLED)
        case_1_2.configure(state=DISABLED)
        case_1_1.configure(state=DISABLED)
        case_1_0.configure(state=DISABLED)
        case_0_2.configure(state=DISABLED)
        case_0_1.configure(state=DISABLED)
        case_0_0.configure(state=DISABLED)
def fait02():
    global c02, i
    i=i+1
    if(i % 2 ==0):
    
        c02=1
    
        case_0_2.configure(image=x)
        case_0_2.configure(state=DISABLED)
    else :
        case_0_2.configure(image=y)
        case_0_2.configure(state=DISABLED)
        c02=2
    if ((c00==1 and c01==1 and c02==1)or (c10==1 and c11==1 and c12==1)or (c20==1 and c21==1 and c22==1)or (c00==1 and c10==1 and c20==1)or (c01==1 and c11==1 and c21==1)or (c02==1 and c12==1 and c22==1)or (c00==1 and c11==1 and c22==1)or (c02==1 and c11==1 and c20==1) )or ((c00==2 and c01==2 and c02==2)or (c10==2 and c11==2 and c12==2)or (c20==2 and c21==2 and c22==2)or (c00==2 and c10==2 and c20==2)or (c01==2 and c11==2 and c21==2)or (c02==2 and c12==2 and c22==2)or (c00==2 and c11==2 and c22==2)or (c02==2 and c11==2 and c20==2)) :
        resultat.configure(text="win")
        case_2_2.configure(state=DISABLED)
        case_2_1.configure(state=DISABLED)
        case_2_0.configure(state=DISABLED)
        case_1_2.configure(state=DISABLED)
        case_1_1.configure(state=DISABLED)
        case_1_0.configure(state=DISABLED)
        case_0_2.configure(state=DISABLED)
        case_0_1.configure(state=DISABLED)
        case_0_0.configure(state=DISABLED)
def fait10():
    global c10,i
    i=i+1
    if(i % 2 ==0):
        case_1_0.configure(image=x)
        case_1_0.configure(state=DISABLED)
        c10=1
    else :
        case_1_0.configure(image=y)
        case_1_0.configure(state=DISABLED)
        c10=2
    if ((c00==1 and c01==1 and c02==1)or (c10==1 and c11==1 and c12==1)or (c20==1 and c21==1 and c22==1)or (c00==1 and c10==1 and c20==1)or (c01==1 and c11==1 and c21==1)or (c02==1 and c12==1 and c22==1)or (c00==1 and c11==1 and c22==1)or (c02==1 and c11==1 and c20==1) )or ((c00==2 and c01==2 and c02==2)or (c10==2 and c11==2 and c12==2)or (c20==2 and c21==2 and c22==2)or (c00==2 and c10==2 and c20==2)or (c01==2 and c11==2 and c21==2)or (c02==2 and c12==2 and c22==2)or (c00==2 and c11==2 and c22==2)or (c02==2 and c11==2 and c20==2)) :
        resultat.configure(text="win")
        case_2_2.configure(state=DISABLED)
        case_2_1.configure(state=DISABLED)
        case_2_0.configure(state=DISABLED)
        case_1_2.configure(state=DISABLED)
        case_1_1.configure(state=DISABLED)
        case_1_0.configure(state=DISABLED)
        case_0_2.configure(state=DISABLED)
        case_0_1.configure(state=DISABLED)
        case_0_0.configure(state=DISABLED) 
def fait11():
    global c11,i
       
    i=i+1
    if(i % 2 ==0):
        c11=1
        case_1_1.configure(image=x)
        case_1_1.configure(state=DISABLED)
    else :
        c11=2
        case_1_1.configure(image=y)
        case_1_1.configure(state=DISABLED)
    if ((c00==1 and c01==1 and c02==1)or (c10==1 and c11==1 and c12==1)or (c20==1 and c21==1 and c22==1)or (c00==1 and c10==1 and c20==1)or (c01==1 and c11==1 and c21==1)or (c02==1 and c12==1 and c22==1)or (c00==1 and c11==1 and c22==1)or (c02==1 and c11==1 and c20==1) )or ((c00==2 and c01==2 and c02==2)or (c10==2 and c11==2 and c12==2)or (c20==2 and c21==2 and c22==2)or (c00==2 and c10==2 and c20==2)or (c01==2 and c11==2 and c21==2)or (c02==2 and c12==2 and c22==2)or (c00==2 and c11==2 and c22==2)or (c02==2 and c11==2 and c20==2)) :
        resultat.configure(text="win")
        case_2_2.configure(state=DISABLED)
        case_2_1.configure(state=DISABLED)
        case_2_0.configure(state=DISABLED)
        case_1_2.configure(state=DISABLED)
        case_1_1.configure(state=DISABLED)
        case_1_0.configure(state=DISABLED)
        case_0_2.configure(state=DISABLED)
        case_0_1.configure(state=DISABLED)
        case_0_0.configure(state=DISABLED)
def fait12():
    global c12,i
    
    i=i+1
    if(i % 2 ==0):
        c12=1
        case_1_2.configure(image=x)
        case_1_2.configure(state=DISABLED)
    else :
        c12=2
        case_1_2.configure(image=y)
        case_1_2.configure(state=DISABLED)
    if ((c00==1 and c01==1 and c02==1)or (c10==1 and c11==1 and c12==1)or (c20==1 and c21==1 and c22==1)or (c00==1 and c10==1 and c20==1)or (c01==1 and c11==1 and c21==1)or (c02==1 and c12==1 and c22==1)or (c00==1 and c11==1 and c22==1)or (c02==1 and c11==1 and c20==1) )or ((c00==2 and c01==2 and c02==2)or (c10==2 and c11==2 and c12==2)or (c20==2 and c21==2 and c22==2)or (c00==2 and c10==2 and c20==2)or (c01==2 and c11==2 and c21==2)or (c02==2 and c12==2 and c22==2)or (c00==2 and c11==2 and c22==2)or (c02==2 and c11==2 and c20==2)) :
        resultat.configure(text="win")
        case_2_2.configure(state=DISABLED)
        case_2_1.configure(state=DISABLED)
        case_2_0.configure(state=DISABLED)
        case_1_2.configure(state=DISABLED)
        case_1_1.configure(state=DISABLED)
        case_1_0.configure(state=DISABLED)
        case_0_2.configure(state=DISABLED)
        case_0_1.configure(state=DISABLED)
        case_0_0.configure(state=DISABLED)
def fait20():
    global c20,i
   
    i=i+1
    if(i % 2 ==0):
        c20=1
        case_2_0.configure(image=x)
        case_2_0.configure(state=DISABLED)
    else :
         c20=2
         case_2_0.configure(image=y)
         case_2_0.configure(state=DISABLED)
    if ((c00==1 and c01==1 and c02==1)or (c10==1 and c11==1 and c12==1)or (c20==1 and c21==1 and c22==1)or (c00==1 and c10==1 and c20==1)or (c01==1 and c11==1 and c21==1)or (c02==1 and c12==1 and c22==1)or (c00==1 and c11==1 and c22==1)or (c02==1 and c11==1 and c20==1) )or ((c00==2 and c01==2 and c02==2)or (c10==2 and c11==2 and c12==2)or (c20==2 and c21==2 and c22==2)or (c00==2 and c10==2 and c20==2)or (c01==2 and c11==2 and c21==2)or (c02==2 and c12==2 and c22==2)or (c00==2 and c11==2 and c22==2)or (c02==2 and c11==2 and c20==2)) :
        resultat.configure(text="win")
        case_2_2.configure(state=DISABLED)
        case_2_1.configure(state=DISABLED)
        case_2_0.configure(state=DISABLED)
        case_1_2.configure(state=DISABLED)
        case_1_1.configure(state=DISABLED)
        case_1_0.configure(state=DISABLED)
        case_0_2.configure(state=DISABLED)
        case_0_1.configure(state=DISABLED)
        case_0_0.configure(state=DISABLED)
def fait21():
    global c21,i
    
    i=i+1
    if(i % 2 ==0):
        c21=1
        case_2_1.configure(image=x)
        case_2_1.configure(state=DISABLED)
    else :
        c21=2
        case_2_1.configure(image=y)
        case_2_1.configure(state=DISABLED)
    if ((c00==1 and c01==1 and c02==1)or (c10==1 and c11==1 and c12==1)or (c20==1 and c21==1 and c22==1)or (c00==1 and c10==1 and c20==1)or (c01==1 and c11==1 and c21==1)or (c02==1 and c12==1 and c22==1)or (c00==1 and c11==1 and c22==1)or (c02==1 and c11==1 and c20==1) )or ((c00==2 and c01==2 and c02==2)or (c10==2 and c11==2 and c12==2)or (c20==2 and c21==2 and c22==2)or (c00==2 and c10==2 and c20==2)or (c01==2 and c11==2 and c21==2)or (c02==2 and c12==2 and c22==2)or (c00==2 and c11==2 and c22==2)or (c02==2 and c11==2 and c20==2)) :
        resultat.configure(text="win")
        case_2_2.configure(state=DISABLED)
        case_2_1.configure(state=DISABLED)
        case_2_0.configure(state=DISABLED)
        case_1_2.configure(state=DISABLED)
        case_1_1.configure(state=DISABLED)
        case_1_0.configure(state=DISABLED)
        case_0_2.configure(state=DISABLED)
        case_0_1.configure(state=DISABLED)
        case_0_0.configure(state=DISABLED)
def fait22():
    global c22,i
    
    i=i+1
    if(i % 2 ==0):
        c22=1
        case_2_2.configure(image=x)
        case_2_2.configure(state=DISABLED)
    else :
        c22=2
        case_2_2.configure(image=y)
        case_2_2.configure(state=DISABLED)
    if ((c00==1 and c01==1 and c02==1)or (c10==1 and c11==1 and c12==1)or (c20==1 and c21==1 and c22==1)or (c00==1 and c10==1 and c20==1)or (c01==1 and c11==1 and c21==1)or (c02==1 and c12==1 and c22==1)or (c00==1 and c11==1 and c22==1)or (c02==1 and c11==1 and c20==1) )or ((c00==2 and c01==2 and c02==2)or (c10==2 and c11==2 and c12==2)or (c20==2 and c21==2 and c22==2)or (c00==2 and c10==2 and c20==2)or (c01==2 and c11==2 and c21==2)or (c02==2 and c12==2 and c22==2)or (c00==2 and c11==2 and c22==2)or (c02==2 and c11==2 and c20==2)) :
        resultat.configure(text="win")
        case_2_2.configure(state=DISABLED)
        case_2_1.configure(state=DISABLED)
        case_2_0.configure(state=DISABLED)
        case_1_2.configure(state=DISABLED)
        case_1_1.configure(state=DISABLED)
        case_1_0.configure(state=DISABLED)
        case_0_2.configure(state=DISABLED)
        case_0_1.configure(state=DISABLED)
        case_0_0.configure(state=DISABLED)
def replayC():
    global i,c00,c01,c02,c10,c11,c12,c20,c21,c22
    case_2_2.configure(state=NORMAL)
    case_2_1.configure(state=NORMAL)
    case_2_0.configure(state=NORMAL)
    case_1_2.configure(state=NORMAL)
    case_1_1.configure(state=NORMAL)
    case_1_0.configure(state=NORMAL)
    case_0_2.configure(state=NORMAL)
    case_0_1.configure(state=NORMAL)
    case_0_0.configure(state=NORMAL)
    case_2_2.configure(image=blank)
    case_2_1.configure(image=blank)
    case_2_0.configure(image=blank)
    case_1_2.configure(image=blank)
    case_1_1.configure(image=blank)
    case_1_0.configure(image=blank)
    case_0_2.configure(image=blank)
    case_0_1.configure(image=blank)
    case_0_0.configure(image=blank)
    i=0
    c00=0
    c01=0
    c02=0
    c10=0
    c11=0
    c12=0
    c20=0
    c21=0
    c22=0
    resultat.configure(text="")
    
##########################
from tkinter import *
i=0
c00=0
c01=0
c02=0
c10=0
c11=0
c12=0
c20=0
c21=0
c22=0
mw=Tk()
blank=PhotoImage(file="rien.gif")
x=PhotoImage(file="x.gif")
y=PhotoImage(file="o.gif")
case_0_0=Button(mw,image=blank,command=fait00)
case_0_0.grid(row=0,column=0)
case_0_1=Button(mw,image=blank,command=fait01)
case_0_1.grid(row=0,column=1)
case_0_2=Button(mw,image=blank,command=fait02)
case_0_2.grid(row=0,column=2)
case_1_0=Button(mw,image=blank,command=fait10)
case_1_0.grid(row=1,column=0)
case_1_1=Button(mw,image=blank,command=fait11)
case_1_1.grid(row=1,column=1)
case_1_2=Button(mw,image=blank,command=fait12)
case_1_2.grid(row=1,column=2)
case_2_0=Button(mw,image=blank,command=fait20)
case_2_0.grid(row=2,column=0)
case_2_1=Button(mw,image=blank,command=fait21)
case_2_1.grid(row=2,column=1)
case_2_2=Button(mw,image=blank,command=fait22)
case_2_2.grid(row=2,column=2)
replayB=Button(mw,text="replay",command=replayC)
replayB.grid(row=4,column=1)
resultat = Label(mw,text=" ")
resultat.grid(row=3,column=1)
