# Take a long sentence and count how many times a specific word appears, ignoring case sensitivity.

sentence = input("Enter a sentence:")
word = input("Enter a word:")

sentence = sentence.lower()
word = word.lower()

words = sentence.split()

count = 0

for w in words:
    if w == word:
        count += 1

print("", word, "apperas", "", count, "times")