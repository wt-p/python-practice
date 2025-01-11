# 自分の回答
t = (1, '2', 3, '4', 5)
num = ''
for v in t:
    num += str(v)
print(f'変換後の数値 : {int(num)}')

# 回答
t = (1, '2', 3, '4', 5)

# タプルの中身を全て文字型に変換する
str_t = (str(v) for v in t)

# タプル->文字型
converted_int = int(''.join(str_t))
print(f'変換後の数値 : {converted_int}')