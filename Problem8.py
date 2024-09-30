# Multiplication of the given numberusing function

def multi(n):
    for i in range(1,11):
        m =n*i
        print(f"{n} X {i} = {m}")
    print()
    

n = int(input("Enter the number : "))
multi(n)