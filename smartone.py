def best_choice():
    global list_choice,c00,c01,c02,c10,c11,c12,c20,c21,c22,t
    i=0
    list_choice=[0,0,0,0,0,0,0,0,0]
    ### choose 00
    if(c00==0):
        if((c01==0 or c01==2) and (c02==0 or c02==1)):
            i=i+1
        if ((c10==0 or c10==2) and (c20==0 or c20==1)):
            i=i+1
        if ((c11==0 or c11==2) and (c22==0 or c22==1)):
            i=i+1
        list_choice[0]=i
        ###put i in array
    if(c01==0):
        i=0
        if((c00==0 or c00==2) and (c02==0 or c02==1)):
            i=i+1
        if ((c11==0 or c11==2) and (c21==0 or c21==1)):
            i=i+1
        list_choice[1]=i
        ###put i in array
    if(c02==0):
        i=0
        if((c01==0 or c01==2) and (c00==0 or c00==1)):
            i=i+1
        if ((c12==0 or c12==2) and (c22==0 or c22==1)):
            i=i+1
        list_choice[2]=i
        ###put i in array
    if(c10==0):
        i=0
        if((c00==0 or c00==2) and (c20==0 or c20==1)):
            i=i+1
        if ((c11==0 or c11==2) and (c12==0 or c12==1)):
            i=i+1
        list_choice[3]=i
        ###put i in array
    if(c11==0):
        i=0
        if((c10==0 or c10==2) and (c12==0 or c12==1)):
            i=i+1
        if ((c01==0 or c01==2) and (c21==0 or c21==1)):
            i=i+1
        if ((c00==0 or c00==2) and (c22==0 or c22==1)):
            i=i+1
        list_choice[4]=i
        ###put i in array
    if(c12==0):
        i=0
        if((c02==0 or c02==2) and (c22==0 or c22==1)):
            i=i+1
        if ((c10==0 or c10==2) and (c11==0 or c11==1)):
            i=i+1
        list_choice[5]=i
        ###put i in array
    if(c20==0):
        i=0
        if((c21==0 or c21==2) and (c22==0 or c22==1)):
            i=i+1
        if ((c10==0 or c10==2) and (c00==0 or c00==1)):
            i=i+1
        list_choice[6]=i
        ###put i in array
    if(c21==0):
        i=0
        if((c20==0 or c20==2) and (c22==0 or c22==1)):
            i=i+1
        if ((c11==0 or c11==2) and (c01==0 or c01==1)):
            i=i+1
        list_choice[7]=i
        ###put i in array
    if(c22==0):
        i=0
        if((c20==0 or c20==2) and (c21==0 or c21==1)):
            i=i+1
        if ((c12==0 or c12==2) and (c02==0 or c02==1)):
            i=i+1
        if ((c11==0 or c11==2) and (c00==0 or c00==1)):
            i=i+1
        list_choice[8]=i
     
    if ( c00==1 and c01==1 and c02==0  ):
        c02=2
        case_0_2.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c00==1 and c02==1 and c01==0 ):
            c01=2
            case_0_1.configure(image=y,state=DISABLED)
            t=1
            return t
    elif ( c02==1 and c01==1 and c00==0):
            c00=2
            case_0_0.configure(image=y,state=DISABLED)
            t=1
            return t
    elif ( c10==1 and c11==1 and c12==0 ):
            c12=2
            case_1_2.configure(image=y,state=DISABLED)
            t=1
            return t
    elif ( c10==1 and c12==1 and c11==0):
            c11=2
            case_0_2.configure(image=y,state=DISABLED)
            t=1
            return t
    elif ( c11==1 and c12==1 and c10==0):
        c10=2
        case_1_0.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c20==1 and c21==1 and  c22==0 ):
        c22=2
        case_2_2.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c20==1 and c22==1 and c21==0):
        c21=2
        case_2_1.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c21==1 and c22==1 and c20==0 ):
        c20=2
        case_2_0.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c00==1 and c10==1 and c20==0):
        c20=2
        case_2_0.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c00==1 and c20==1 and c10==0 ):
        c10=2
        case_1_0.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c10==1 and c20==1 and c00==0 ):
        c00=2
        case_0_0.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c00==1 and c11==1 and c22==0 ):
        c22=2
        case_2_2.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c00==1 and c22==1 and c11==0 ):
        c11=2
        case_1_1.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c11==1 and c22==1 and c00==0):
        c00=2
        case_0_0.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c01==1 and c11==1 and c21==0):
        c21=2
        case_2_1.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c01==1 and c21==1 and c11==0):
        c11=2
        case_1_1.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c21==1 and c11==1 and c01==0):
        c01=2
        case_0_1.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c02==1 and c12==1 and c22==0):
        c22=2
        case_2_2.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c02==1 and c22==1 and c12==0):
        c12=2
        case_1_2.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c12==1 and c22==1 and c02==0 ):
        c02=2
        case_0_2.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c02==1 and c11==1 and c20==0 ):
        c20=2
        case_2_0.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c02==1 and c20==1 and c11==0 ):
        c11=2
        case_1_1.configure(image=y,state=DISABLED)
        t=1
        return t
    elif ( c20==1 and c11==1  and c02==0 ):
        c02=2
        case_0_2.configure(image=y,state=DISABLED)
        t=1
        return t
    else :
        x=5
    t=0
    return t






def is_there_chance_towin():
    global c00,c01,c02,c10,c11,c12,c20,c21,c22
    x=0
    if ( c00==2 and c01==2 and c02==0 ):
        c02=2
        case_0_2.configure(image=y)
        x=1
        return x
    if ( c00==2 and c02==2 and c01==0):
            c01=2
            case_0_1.configure(image=y)
            x=1
            return  x
    if ( c02==2 and c01==2 and c00==0 ):
            c00=2
            x=1
            
            case_0_0.configure(image=y)
            return  x
    if ( c10==2 and c11==2 and c12==0):
            c12=2
            x=1
            
            case_1_2.configure(image=y)
            return x
    if ( c10==2 and c12==2 and c11==0):
            c11=2
            x=1
            
            case_0_2.configure(image=y)
            return x
    if ( c11==2 and c12==2 and c10==0 ):
        c10=2
        x=1
        
        case_1_0.configure(image=y)
        return x
    if ( c20==2 and c21==2  and c22==0):
        c22=2
        x=1
        
        case_0_2.configure(image=y)
        return x
    if ( c20==2 and c22==2 and c21==0):
        c21=2
        x=1
        
        case_2_1.configure(image=y)
        return x
    if ( c21==2 and c22==2 and c20==0):
        c20=2
        x=1
        
        case_2_0.configure(image=y)
        return x
    if ( c00==2 and c10==2 and c20==0 ):
        c20=2
        x=1
        case_2_0.configure(image=y)
        return x
    if ( c00==2 and c20==2 and c10==0):
        c10=2
        x=1
        
        case_1_0.configure(image=y)
        return x
    if ( c10==2 and c20==2 and c00==0 ):
        c00=2
        x=1
        
        case_0_0.configure(image=y)
        return x
    if ( c00==2 and c11==2 and c22==0):
        c22=2
        x=1
        
        case_2_2.configure(image=y)
        return x
    if ( c00==2 and c22==2 and c11==0):
        c11=2
        x=1
        
        case_1_1.configure(image=y)
        return x
    if ( c11==2 and c22==2 and c00==0):
        c00=2
        x=1
        
        case_0_0.configure(image=y)
        return x
    if ( c01==2 and c11==2 and c21==0 ):
        c21=2
        x=1
        
        case_2_1.configure(image=y)
        return x
    if ( c01==2 and c21==2 and c11==0):
        c11=2
        x=1
        
        case_1_1.configure(image=y)
        return x
    if ( c21==2 and c11==2 and c01==0 ):
        c01=2
        x=1
        
        case_0_1.configure(image=y)
        return x
    if ( c02==2 and c12==2 and c22==0):
        c22=2
        x=1
        
        case_2_2.configure(image=y)
        return x
    if ( c02==2 and c22==2 and c12==0 ):
        c12=2
        x=1
        
        case_1_2.configure(image=y)
        return x
    if ( c12==2 and c22==2 and c02==0 ):
        c02=2
        x=1
        
        case_0_2.configure(image=y)
        return x
    if ( c02==2 and c11==2 and c20==0 ):
        c20=2
        x=1
       
        case_2_0.configure(image=y)
        return x
    if ( c02==2 and c20==2 and c11==0 ):
        c11=2
        x=1
        
        case_1_1.configure(image=y)
        return x
    if ( c20==2 and c11==2 and c02==0 ):
        c02=2
        x=1
        
        case_0_2.configure(image=y)
        return x
    
    x=0
    return x


    















def fait00():
    global c00,list_choice,c01,c02,c10,c11,c12,c20,c21,c22
    c00=1
    case_0_0.configure(image=x)
    case_0_0.configure(state=DISABLED)
    winner=is_there_chance_towin()
    print(winner)
    if(winner==0):
        best_choice ()
        d=list_choice[0]
        k=0
        for p in range (1,9) :
           
            if (d<=list_choice[p]):
                
                k=p
                d=list_choice[p]
        if (t==0):   
            if (k==0):
                if (c00==0):
                    
                    case_0_0.configure(image=y)
                    case_0_0.configure(state=DISABLED)
                    c00=2
            if (k==1):
                if (c01==0):
                    
                    case_0_1.configure(image=y)
                    case_0_1.configure(state=DISABLED)
                    c01=2
            if (k==2):
                if (c02==0):
                    
                    case_0_2.configure(image=y)
                    case_0_2.configure(state=DISABLED)
                    c02=2
            if (k==3):
                if (c01==0):
                    case_1_0.configure(image=y)
                    case_1_0.configure(state=DISABLED)
                    c10=2
            if (k==4):
                if(c11==0):
                    case_1_1.configure(image=y)
                    case_1_1.configure(state=DISABLED)
                    c11=2
            if (k==5):
                if (c12==0):
                    case_1_2.configure(image=y)
                    case_1_2.configure(state=DISABLED)
                    c12=2
            if (k==6):
                if (c20==0):
                    case_2_0.configure(image=y)
                    case_2_0.configure(state=DISABLED)
                    c20=2
            if (k==7):
                if(c21==0):
                    case_2_1.configure(image=y)
                    case_2_1.configure(state=DISABLED)
                    c21=2
            if (k==8):
                if(c22==0):
                    case_2_2.configure(image=y)
                    case_2_2.configure(state=DISABLED)
                    c22=2
    
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
    global c00,list_choice,c01,c02,c10,c11,c12,c20,c21,c22,t
    
    
    c01=1
    
    case_0_1.configure(image=x)
    case_0_1.configure(state=DISABLED)
    winner=is_there_chance_towin()
    print(winner)
    if(winner==0):
        best_choice ()
        d=list_choice[0]
        k=0
        for p in range (1,9) :
            if (d<=list_choice[p]):
                k=p
                d=list_choice[p]
        print(t,k)
        if (t==0):
            print("hello")
            if (k==0):
                case_0_0.configure(image=y)
                case_0_0.configure(state=DISABLED)
                c00=2
            if (k==1):
                case_0_1.configure(image=y)
                case_0_1.configure(state=DISABLED)
                c01=2
            if (k==2):
                case_0_2.configure(image=y)
                case_0_2.configure(state=DISABLED)
                c02=2
            if (k==3):
                case_1_0.configure(image=y)
                case_1_0.configure(state=DISABLED)
                c10=2
            if (k==4):
                case_1_1.configure(image=y)
                case_1_1.configure(state=DISABLED)
                c11=2
            if (k==5):
                    case_1_2.configure(image=y)
                    case_1_2.configure(state=DISABLED)
                    c12=2
            if (k==6):
                case_2_0.configure(image=y)
                case_2_0.configure(state=DISABLED)
                c20=2
            if (k==7):
                case_2_1.configure(image=y)
                case_2_1.configure(state=DISABLED)
                c21=2
            if (k==8):
                case_2_2.configure(image=y)
                case_2_2.configure(state=DISABLED)
                c22=2
    
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
    global c00,list_choice,c01,c02,c10,c11,c12,c20,c21,c22
    
    
    c02=1
    
    case_0_2.configure(image=x)
    case_0_2.configure(state=DISABLED)
    winner=is_there_chance_towin()
    if(winner==0):
        best_choice ()
        d=list_choice[0]
        k=0
        for p in range (1,9) :
            if (d<=list_choice[p]):
                k=p
                d=list_choice[p]
        if (t==0):
            if (k==0):
                case_0_0.configure(image=y)
                case_0_0.configure(state=DISABLED)
                c00=2
            if (k==1):
                case_0_1.configure(image=y)
                case_0_1.configure(state=DISABLED)
                c01=2
            if (k==2):
                case_0_2.configure(image=y)
                case_0_2.configure(state=DISABLED)
                c02=2
            if (k==3):
                case_1_0.configure(image=y)
                case_1_0.configure(state=DISABLED)
                c10=2
            if (k==4):
                case_1_1.configure(image=y)
                case_1_1.configure(state=DISABLED)
                c11=2
            if (k==5):
                case_1_2.configure(image=y)
                case_1_2.configure(state=DISABLED)
                c12=2
            if (k==6):
                case_2_0.configure(image=y)
                case_2_0.configure(state=DISABLED)
                c20=2
            if (k==7):
                case_2_1.configure(image=y)
                case_2_1.configure(state=DISABLED)
                c21=2
            if (k==8):
                case_2_2.configure(image=y)
                case_2_2.configure(state=DISABLED)
                c22=2
    
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
    global c00,list_choice,c01,c02,c10,c11,c12,c20,c21,c22
    
    case_1_0.configure(image=x)
    case_1_0.configure(state=DISABLED)
    c10=1
    winner=is_there_chance_towin()
    
    if(winner==0):
        best_choice ()
        
        d=list_choice[0]
        k=0
        
        for p in range (1,9) :
            
            if (d<=list_choice[p]):
                k=p
                d=list_choice[p]
        print (t,k)
        if (t==0):
            if (k==0):
                case_0_0.configure(image=y)
                case_0_0.configure(state=DISABLED)
                c00=2
            if (k==1):
                case_0_1.configure(image=y)
                case_0_1.configure(state=DISABLED)
                c01=2
            if (k==2):
                case_0_2.configure(image=y)
                case_0_2.configure(state=DISABLED)
                c02=2
            if (k==3):
                case_1_0.configure(image=y)
                case_1_0.configure(state=DISABLED)
                c10=2
            if (k==4):
                case_1_1.configure(image=y)
                case_1_1.configure(state=DISABLED)
                c11=2
            if (k==5):
                case_1_2.configure(image=y)
                case_1_2.configure(state=DISABLED)
                c12=2
            if (k==6):
                case_2_0.configure(image=y)
                case_2_0.configure(state=DISABLED)
                c20=2
            if (k==7):
                case_2_1.configure(image=y)
                case_2_1.configure(state=DISABLED)
                c21=2
            if (k==8):
                case_2_2.configure(image=y)
                case_2_2.configure(state=DISABLED)
                c22=2
    
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
    global c00,list_choice,c01,c02,c10,c11,c12,c20,c21,c22
       
    
    c11=1
    case_1_1.configure(image=x)
    case_1_1.configure(state=DISABLED)
    winner=is_there_chance_towin()
    if(winner==0):
        best_choice ()
        d=list_choice[0]
        k=0
        for p in range (1,9) :
            if (d<=list_choice[p]):
                k=p
                d=list_choice[p]
        if (t==0):
            if (k==0):
                case_0_0.configure(image=y)
                case_0_0.configure(state=DISABLED)
                c00=2
            if (k==1):
                case_0_1.configure(image=y)
                case_0_1.configure(state=DISABLED)
                c01=2
            if (k==2):
                case_0_2.configure(image=y)
                case_0_2.configure(state=DISABLED)
                c02=2
            if (k==3):
                case_1_0.configure(image=y)
                case_1_0.configure(state=DISABLED)
                c10=2
            if (k==4):
                case_1_1.configure(image=y)
                case_1_1.configure(state=DISABLED)
                c11=2
            if (k==5):
                case_1_2.configure(image=y)
                case_1_2.configure(state=DISABLED)
                c12=2
            if (k==6):
                case_2_0.configure(image=y)
                case_2_0.configure(state=DISABLED)
                c20=2
            if (k==7):
                case_2_1.configure(image=y)
                case_2_1.configure(state=DISABLED)
                c21=2
            if (k==8):
                case_2_2.configure(image=y)
                case_2_2.configure(state=DISABLED)
                c22=2
    
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
    global c00,list_choice,c01,c02,c10,c11,c12,c20,c21,c22
    
    
    c12=1
    case_1_2.configure(image=x)
    case_1_2.configure(state=DISABLED)
    winner=is_there_chance_towin()
    if(winner==0):
        best_choice ()
        d=list_choice[0]
        k=0
        for p in range (1,9) :
            if (d<=list_choice[p]):
                k=p
                d=list_choice[p]
        if (t==0):
            if (k==0):
                case_0_0.configure(image=y)
                case_0_0.configure(state=DISABLED)
                c00=2
            if (k==1):
                case_0_1.configure(image=y)
                case_0_1.configure(state=DISABLED)
                c01=2
            if (k==2):
                case_0_2.configure(image=y)
                case_0_2.configure(state=DISABLED)
                c02=2
            if (k==3):
                case_1_0.configure(image=y)
                case_1_0.configure(state=DISABLED)
                c10=2
            if (k==4):
                case_1_1.configure(image=y)
                case_1_1.configure(state=DISABLED)
                c11=2
            if (k==5):
                case_1_2.configure(image=y)
                case_1_2.configure(state=DISABLED)
                c12=2
            if (k==6):
                case_2_0.configure(image=y)
                case_2_0.configure(state=DISABLED)
                c20=2
            if (k==7):
                case_2_1.configure(image=y)
                case_2_1.configure(state=DISABLED)
                c21=2
            if (k==8):
                case_2_2.configure(image=y)
                case_2_2.configure(state=DISABLED)
                c22=2
    
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
    global c00,list_choice,c01,c02,c10,c11,c12,c20,c21,c22
    c20=1
    case_2_0.configure(image=x)
    case_2_0.configure(state=DISABLED)
    winner=is_there_chance_towin()
    if(winner==0):
        best_choice ()
        d=list_choice[0]
        k=0
        for p in range (1,9) :
            if (d<=list_choice[p]):
                k=p
                d=list_choice[p]
        if (t==0):
            if (k==0):
                case_0_0.configure(image=y)
                case_0_0.configure(state=DISABLED)
                c00=2
            if (k==1):
                case_0_1.configure(image=y)
                case_0_1.configure(state=DISABLED)
                c01=2
            if (k==2):
                case_0_2.configure(image=y)
                case_0_2.configure(state=DISABLED)
                c02=2
            if (k==3):
                case_1_0.configure(image=y)
                case_1_0.configure(state=DISABLED)
                c10=2
            if (k==4):
                case_1_1.configure(image=y)
                case_1_1.configure(state=DISABLED)
                c11=2
            if (k==5):
                case_1_2.configure(image=y)
                case_1_2.configure(state=DISABLED)
                c12=2
            if (k==6):
                case_2_0.configure(image=y)
                case_2_0.configure(state=DISABLED)
                c20=2
            if (k==7):
                case_2_1.configure(image=y)
                case_2_1.configure(state=DISABLED)
                c21=2
            if (k==8):
                case_2_2.configure(image=y)
                case_2_2.configure(state=DISABLED)
                c22=2
    
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
    global c00,list_choice,c01,c02,c10,c11,c12,c20,c21,c22
    c21=1
    case_2_1.configure(image=x)
    case_2_1.configure(state=DISABLED)
    winner=is_there_chance_towin()
    if(winner==0):
        best_choice ()
        d=list_choice[0]
        k=0
        for p in range (1,9) :
            if (d<=list_choice[p]):
                k=p
                d=list_choice[p]
        if (t==0):
            if (k==0):
                case_0_0.configure(image=y)
                case_0_0.configure(state=DISABLED)
                c00=2
            if (k==1):
                case_0_1.configure(image=y)
                case_0_1.configure(state=DISABLED)
                c01=2
            if (k==2):
                case_0_2.configure(image=y)
                case_0_2.configure(state=DISABLED)
                c02=2
            if (k==3):
                case_1_0.configure(image=y)
                case_1_0.configure(state=DISABLED)
                c10=2
            if (k==4):
                case_1_1.configure(image=y)
                case_1_1.configure(state=DISABLED)
                c11=2
            if (k==5):
                case_1_2.configure(image=y)
                case_1_2.configure(state=DISABLED)
                c12=2
            if (k==6):
                case_2_0.configure(image=y)
                case_2_0.configure(state=DISABLED)
                c20=2
            if (k==7):
                case_2_1.configure(image=y)
                case_2_1.configure(state=DISABLED)
                c21=2
            if (k==8):
                case_2_2.configure(image=y)
                case_2_2.configure(state=DISABLED)
                c22=2
    
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
    global c00,list_choice,c01,c02,c10,c11,c12,c20,c21,c22
    c22=1
    case_2_2.configure(image=x)
    case_2_2.configure(state=DISABLED)
    winner=is_there_chance_towin()
    if(winner==0):
        best_choice ()
        d=list_choice[0]
        k=0
        for p in range (1,9) :
            if (d<=list_choice[p]):
                k=p
                d=list_choice[p]
        if (t==0):
            if (k==0):
                case_0_0.configure(image=y)
                case_0_0.configure(state=DISABLED)
                c00=2
            if (k==1):
                case_0_1.configure(image=y)
                case_0_1.configure(state=DISABLED)
                c01=2
            if (k==2):
                case_0_2.configure(image=y)
                case_0_2.configure(state=DISABLED)
                c02=2
            if (k==3):
                case_1_0.configure(image=y)
                case_1_0.configure(state=DISABLED)
                c10=2
            if (k==4):
                case_1_1.configure(image=y)
                case_1_1.configure(state=DISABLED)
                c11=2
            if (k==5):
                case_1_2.configure(image=y)
                case_1_2.configure(state=DISABLED)
                c12=2
            if (k==6):
                case_2_0.configure(image=y)
                case_2_0.configure(state=DISABLED)
                c20=2
            if (k==7):
                case_2_1.configure(image=y)
                case_2_1.configure(state=DISABLED)
                c21=2
            if (k==8):
                case_2_2.configure(image=y)
                case_2_2.configure(state=DISABLED)
                c22=2
	
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
    x=0
    for p in range(1,9) :
        list_choice[p]=0    
    
    
##########################
from tkinter import *
t=5
winner=100
list_choice=[0,0,0,0,0,0,0,0,0]
x=0
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
k00=False
k01=False
k02=False
k10=False
k11=False
k12=False
k20=False
k21=False
k22=False
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
