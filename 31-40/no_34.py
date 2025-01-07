# 自分の回答
l = ['1', 2, '3', 4, '5', 6, '7', 8, '9', 10]
even_index_list = []
for i in range(len(l)):
    if i % 2 == 0:
        even_index_list.append(l[i])
print(f"偶数のインデックス番号 : {even_index_list}")

# 回答
l = ['1', 2, '3', 4, '5', 6, '7', 8, '9', 10]
print(f'偶数のインデックス番号 : {l[::2]}')