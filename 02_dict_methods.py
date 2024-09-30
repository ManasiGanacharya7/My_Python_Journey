a= {
    "Manasi" : 89,
    "Abhay" : 80,
    "Yog" : 85,
    "Roops" : 79
}

print(a,type(a))
print(a.items())
print(a.keys())
print(a.values())
a.update({"Hro":98, "Micky":45})
print(a)

print(a.get("Yog"))
value= a.pop('Manasi')  # Removes and returns the value 1
print(a)
