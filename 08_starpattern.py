# print *
print("*")
#-----------------------------
print("-")

# print * in one by one 
i = None
for i in range(5):
    print("*")

# print * in one line n no of times
#-----------------------------
print("-")
i = None
for i in range(5):
    print("*",end=" ")

# print * in n*n using j
#----------------------------- 
print("-") 

for i in range(5):
    for j in range(5):
        print("* ",end = " ")
    print()

# print * in triangle
#----------------------------- 
print("-") 

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()


# print * in triangle
#----------------------------- 
print("-") 

for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()
    
# print * in exact triangle
#----------------------------- 
print("-") 

#----------------------------- 
print("trying to print triangle") 
n = int(input("l Enter number : "))
for i in range( 1,n ):
    for j in range (1,i+1):
        print("*", end="")
        i+=1
        j=i+1
       
    print("")

#----------------------------- 
i=0
j = None

n = int(input("Enter number : "))
for i in range (0,n ):
    for j in range (i+1):
        print("*",end="")
        i+=1
        j=n-1
    print("")
    
#----------------------------- 
i=0
j = None

n = int(input("Enter number : "))
for i in range (i,n ):
    for j in range (n-i):
        print("*",end="")
        i-=1
        j=n-1
    print("")

#Right half pyramid

print("Right half pyramid")

n=5
for i in range(n):
    for j in range(n-i):
        print(" ", end="")

    for k in range(i+1):
        print("*",end= "")

    print()

#Left half pyramid
print("left half pyramid")

n = 6

for i in range(n):
    for j in range(n-i):
        print("*",end="")

    for k in range(i+1):
        print(" ",end="")
    print()

