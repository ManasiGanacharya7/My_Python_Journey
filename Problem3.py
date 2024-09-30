# detect the comment is spam or not

b1 = "Make a lots of Money"
b2 = "Make wealth"
b3 = "click on this link"
b4 = "Get rewards"

msg = input("Enter message : ")

if(b1 in msg or b2 in msg or b3 in msg or b4 in msg):
    print("Spam msg")
else:
    print("Not spam")