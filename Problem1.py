# prog to write table of the given no by user wt for loop

a = int(input("Enter the table you want: "))

for i in range(1,11):
    print(f"{a} * {i} = {a * i}" )
    i+=1