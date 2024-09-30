# write  a prog to see if the student has passed or failed if he requires at least 40% total 
# and atleast 33% per subject assume there are 3 subjects

name = input("Enter your name :")
m1 = int(input("Enter Science Marks :"))
m2 = int(input("Enter Maths Marks :"))
m3 = int(input("Enter History Marks :"))

add = (m1+m2+m3)
total = 300
perc = (add/total)*100

print(add)
print(perc, "%")

if perc>=40 and m1>=33 and m2>=33 and m3>=33:
    print(f"{name} {perc} You are Pass")

else:
    print(f"{name} {perc}you Failed")
