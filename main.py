import random

source_file = "plaintext.txt"
anagram_file = "anagrams.txt"

plaintext = []

with open(source_file, "r") as src:
    plaintext = src.readlines()

anagrams = []

for phrase in plaintext:
    phrase = phrase.strip('\n')
    letters = []
    counter = 0
    while counter < len(phrase):
        if phrase[counter] != " ":
            letters.append(phrase[counter])
        counter += 1

    random.shuffle(letters)
    anagram = ""
    counter = 0
    while counter < len(phrase):
        if phrase[counter] == " ":
            anagram += " "
        else:
            anagram += letters.pop()
        counter += 1

    anagrams.append(anagram)

with open(anagram_file, "w") as dest:
    for anagram in anagrams:
        dest.write(anagram+"\n")