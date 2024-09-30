# WRITE A PROGRAM TO FIND THE GRATEST OF ALL NUMBER

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
num3 = int(input("Enter the number 3 : "))
num4 = int(input("Enter the number 4 : "))

if num1>num2 and num1>num3 and num1>num4 :
    print("n1 is grater!")

elif num2>num1 and num2>num3 and num2>num4 :
    print("print num2 is grater")

elif num3>num1 and num3>num2 and num3>num4:
    print("print num3 is grater")
else:
    print("num4 is grater")