#Prog to find greatest number using function

def greatestnum(n1,n2,n3):
    
    if (n1>n2) and (n1>n3):
        print(f"{n1} is greater")  
    elif (n2>n1) and (n2>n3):
        print(f"{n2} is greater")
    else:
        print(f"{n3} is greater")

greatestnum(0,99,689)