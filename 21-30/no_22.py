# 自分の回答
# first_char = input("1つ目の文字列を入力してください >")
# second_char = input("2つ目の文字列を入力してください >")
# result = ""
# for char in first_char:
#     if char in second_char:
#         result += char
#
# print(f"重複する文字列 : {result}")

# 回答
word1 = input("1つ目の文字列を入力してください >")
word2 = input("2つ目の文字列を入力してください >")

r = ''
for ch in word1:
    if ch in word2 and ch not in r:
        r += ch

print(f"重複する文字列 : {r}")