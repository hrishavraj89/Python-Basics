# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’
f = open("poems.txt", "r")
content = f.read()
if "twinkle" in content or "Twinkle" in content:
    print("Yes, twinkle is present! ")
else:
    print("No, twinkle is not present! ")
f.close()