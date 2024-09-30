age = int(input("Enter your age: "))

if age>=18:
    print("You can apply for driving licence")
    if age==18:
        print("you are 18")
    else:
        print("You are above")

elif age<0:
    print("Age cannot be negative !!!")

elif age==0:
    print("Age is zero")

else:
    print("You can't apply")
print("End of program!")