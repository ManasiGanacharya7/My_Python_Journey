#avg of marks

a = 80
b = 57
c = 79

avg = (a+b+c)/3

print(avg)

#with functions

def average():

    numsub = int(input("Enter the number of subjects : "))
    i = 1
    summ = 0
    for i in range(1,numsub+1):
        a=int(input((f"Enter subject{i} marks: ")))
        i+=1
        summ=summ+a

    print((summ/numsub))

average()
