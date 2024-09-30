# reverse table wt for loop

n = int(input("Enter the number : "))
i = None
for i in range(10,0,-1):
    print(f"{n}X{i} = {n*i}")
    i+=1
print("")