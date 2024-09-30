#function wt return value

def average():

    numsub = int(input("Enter the number of subjects : "))
    i = 1
    summ = 0
    for i in range(1,numsub+1):
        a=int(input((f"Enter subject{i} marks: ")))
        i+=1
        summ=summ+a

    k=(summ/numsub)
    print(k)
    return "ok"
a="hello"
print(a)
average()

