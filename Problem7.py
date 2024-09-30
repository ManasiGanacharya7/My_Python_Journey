# Find the post is talking about "Harry"

post = ["Harry", "harry", "HARRY"]

a = input("enter post : ")

if a.lower() in post:
    print("Post is about Harry")

else:
    print("Not about harry")   