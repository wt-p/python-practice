# 自分の回答
t = (1, [2, 3], '4', (5, 6, 7), '8', (9, 10))
l = [v for v in t if isinstance(v, tuple)]
print(f'タプル内に含まれるタプルの数 : {len(l)}')

# 回答
t = (1, [2, 3], '4', (5, 6, 7), '8', (9, 10))
t_in_tuple = [v for v in t if isinstance(v, tuple)]
print(f'タプル内に含まれるタプルの数 : {len(t_in_tuple)}')