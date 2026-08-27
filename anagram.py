word1 = input("Enter a word: ")
word2 = input("Enter a word: ")

if(sorted(word1) == sorted(word2)):
    print("The words are anagrams")
else:
    print("The words are not anagrams")
