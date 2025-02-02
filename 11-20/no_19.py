# 自分の回答
import re
word = input("文字列を入力してください >")
print(f"作成した文字列 : {re.sub('[aiueo]', '', word)}")

# 回答
vowels = ['a', 'i', 'u', 'e', 'o']

word = input('文字列を入力してください > ')

new_word = ''
for s in word:
    if s in vowels:
        continue
    new_word += s

print(f'作成した文字列 : {new_word}')

# 別解
vowels = ['a', 'i', 'u', 'e', 'o']
word = input('文字列を入力してください > ')

for v in vowels:
    word = word.replace(v, '')

print(f'作成した文字列 : {word}')