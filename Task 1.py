# Caroline
# Loop to iterate from 1 to 10

for i in range(0, 11):
    print(i, end=" ")
print()

for i in range(0, 101, 2):
    print(i, end=" ")
print()

for i in range(20, 0, -2):
    print(i, end=" ")
print()

for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i, end=" ")

import string
counter = 0
counter_nubmer = 0
sentence = input("Please enter a sentence: ")
VOWELS = ("AEIOUaeiou")

for character in sentence:
    if character.isalpha():
        counter += 1
    elif character in string.punctuation:
        counter_nubmer += 1
print(counter)
print(counter_nubmer)

