# WRITE A PROGRAM TO MAKE A LIST OF SEVEN FRUITS ENTERED BY THE USER

fruits = []

fruit1 = input("Enter fruit1 : ")
fruit2 = input("Enter fruit2 : ")
fruit3 = input("Enter fruit3 : ")
fruit4 = input("Enter fruit4 : ")
fruit5 = input("Enter fruit5 : ")
fruit6 = input("Enter fruit6 : ")
fruit7 = input("Enter fruit7 : ")

fruits = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7]
print("The fruits names : ", fruits)

# ---------------------------------------------------------------------

fru = []

for i in range(7):
    fruit = input(f"Enter fruit name  {i+1} :")
    fru.append(fruit)
print("fruits : ",fru)