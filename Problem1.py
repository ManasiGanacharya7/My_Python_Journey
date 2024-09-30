# Write a program to create dict  of hindi words values as their english translation provide user to lookup
tran = {
    "Madat" : "Help",
    "Paisa" : "Money",
    "Billi" : "Cat",
    "Namaste" : "hello"
}

word = input("Enter the word you want meaning of : ")
print(tran[word])

print("-------------------------------------------------------------")
print(tran)
print(tran.values())
print(tran.keys())
