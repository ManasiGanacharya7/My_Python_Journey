s = {} # it will create an empty dict
e = set() #to create empty set use this or it will generate an error
print(type(e))

s = {3,22,6,22,7,6,"Manasi"} #cannot repeat the values
print(s)

s.add(34)
print(s)

s.remove(6)
print(s)

s.discard(7)
print(s)

s1 = {3,5,7,9,8,22}
s2 = {44,65,0,2,1,8,3,5,7,8,22}

set_new = s1.union(s2)
print(set_new)

set_new1 = s1.intersection(s2)
print(set_new1)

set_new2 = s1.difference(s2)
print(set_new2)

set_new3 = s1.issubset(s2)
print(set_new3)

set_new3 = s1.issuperset(s2)
print(set_new3)

set_new3 = s1.isdisjoint(s2)
print(set_new3)