# 自分の回答
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_l = [[ for i in l ] for i in range(3)]
# print(f'3分割したタプル : {new_l}')

# 回答
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_l = [tuple(l[i:i+3]) for i in range(0, 9, 3)]
print(f'3分割したタプル : {new_l}')