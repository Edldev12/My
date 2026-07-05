word = input()
if word.isupper() or (len(word) == 1 and word.islower()) or (word[0].islower() and word[1:].isupper()):
    print(word.swapcase())
else:
    print(word)
