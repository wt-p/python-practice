# 自分の回答
# char = input("文字列を入力してください >")
# if char[0].islower():
#     char = char[0].upper() + char[1:]
# else:
#     char += char
# print(f"変換後の文字列 : {char}")

# 回答
word = input("文字列を入力してください >")
if word[0].islower():
    word = word[0].upper() + word[1:]
else:
    word = word*2
print(f"変換後の文字列 : {word}")