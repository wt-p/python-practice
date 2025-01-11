# 自分の回答
l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_l = [l[i][i] for i in range(3)]
print(f'1行目の値 : {new_l}')
print(f'2行目の値 : {new_l}')
print(f'3行目の値 : {l}')

# 回答
l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for i, row in enumerate(l, start=1):
    a, b, c = row
    print(f'{i}行目の値 : {a} {b} {c}')