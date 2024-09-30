#Write a program take 8 user marks and display unique nos. only

marks = set()

m1 = input("Enter number 1 :")
marks.add(m1)
m1 = input("Enter number 2 :")
marks.add(m1)
m1 = input("Enter number 3 :")
marks.add(m1)
m1 = input("Enter number 4 :")
marks.add(m1)
m1 = input("Enter number 5 :")
marks.add(m1)
m1 = input("Enter number 6 :")
marks.add(m1)

print(marks)
print(marks.union())
