word=input().lower()
vowels='aeiyou'
for i in word:
    if i in vowels:
        word=word.replace(i,'')
new_word=''
for i in word:
    new_word+='.'+i
print(new_word)
