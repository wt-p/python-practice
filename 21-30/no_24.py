# 自分の回答
char = input("英単語を入力してください >")
char_num = len(char)
num = char_num // 2
if char_num % 2 == 0:
    char = char[:num] + "@" + char[num:]
else:
    char = char[:num] + "@" + char[num + 1:]
print(f"変換した英単語 : {char}")

# 回答
word = input("英単語を入力してください >")
count = 0

for _ in word:
    count += 1

index = count // 2

if count % 2 == 0:
    word = word[:index] + "@" + word[index:]
else:
    word = word[:index] + "@" + word[index+1:]
print(f"変換した英単語 : {word}")