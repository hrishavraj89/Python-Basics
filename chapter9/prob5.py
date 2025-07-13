# Repeat program 4 for a list of such words to be censored.

word = ["donkey", "shit", "hell", "dog"]
with open("cencored_words.txt", "r") as f:
    content = f.read()
for words in word:
    content = content.replace(words , "#" * len(word))

with open("cencored_words.txt", "w") as f:
    f.write(content)