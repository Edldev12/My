string=input().strip()
unique_letters = set()

for char in string:
    if char.isalpha():
        unique_letters.add(char.lower())

print(len(unique_letters))
