# 自分の回答
l = [0, '1', 3, 2, '4', 5, '7']
new_l = [l[i] for i in range(len(l)) if int(l[i]) == i]
print(f'インデックスと値が一致 : {new_l}')

# 回答
l = [0, '1', 3, 2, '4', 5, '7']
new_l = [v for i, v in enumerate(l) if i == int(v)]
print(f'インデックスと値が一致 : {new_l}')