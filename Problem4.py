#Recurcive function to find sum of n natural number


def summation(n):
    sum=0
    
    for i in range(1,n+1):
        sum=sum+i
        i+=1
    print(sum)

n = int(input("Enter the n : "))
summation(n)

