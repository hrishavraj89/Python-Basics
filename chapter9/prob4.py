# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 

word = "donkey"
with open("donkey.txt", "r") as f:
    content = f.read()

New_content = content.replace(word, "######")

with open("donkey.txt", "w") as f:
    f.write(New_content)