'''write a prog to print *
                        **
                        ***
                        ****'''

n = int(input("Enter the number : "))

for i in range(n):
    for j in range (0,n-i-1):
        print(" ",end="")

    for j in range(1, i+1):
        print(f"{i}", end="")
    print()

    

#Function to print full pyramid pattern
n=5
for i in range(0,n):
    print(" "*(n-i),end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()