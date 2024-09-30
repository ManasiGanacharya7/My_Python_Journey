# ACCEPT MARKS OF STUDENTS OF 6SUBJECTS AND SORT THEM TOGETHER

a = []

for i in range(6):
    b = input(f"Enter Marks : {i+1} ")
    a.append(b)

print(a)
a.sort()
print(a)