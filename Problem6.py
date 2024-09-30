#wirte a prog to find the factorial of the given number using for loop :

n = int(input("Enter the number : "))
i = 1
fact = 1

for i in range(1,n+1):
    fact= fact*i
    if i==n:
        print("=")
    print(f"{i} X ", end="")

print(fact)