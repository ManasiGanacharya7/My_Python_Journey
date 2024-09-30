# Prog to find celsius to convert faranite using function
''''
c = 5*(f-32/9)'''

def f_to_c(f):
    celcicus = 5*(f-32)/9
    print(f"{celcicus}°C")

f = int(input("Enter f : "))
f_to_c(f)

