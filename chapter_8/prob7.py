# Write a python function to remove a given word from a list ad strip it at the same
# time.

def remove_strip(l, word_to_remove):
    new_list = []
    for word in l:
        stripped_word = word.strip()
        if stripped_word != word_to_remove:
            new_list.append(stripped_word)
    return new_list

l = ["apple", "mango", "banana", "litchi"]
print(remove_strip(l, "banana"))