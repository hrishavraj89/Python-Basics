spam = "harry"
comment = input("Enter your comment: ")
if(spam.lower() in comment.lower()):
    print("This is a valid comment")

else:
    print("This is not a valid comment")