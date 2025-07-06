spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

comment = input("Enter you comment: ")

if(spam1 in comment or spam2 in comment or spam3 in comment or spam4 in comment):
    print("Spam detected")