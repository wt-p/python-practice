# 自分の回答
d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
new_d = sorted(d.items(), key=lambda x: x[1])
print(f'最小のValueを持つKey : {new_d[0][0]}')

# 回答
d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
key_with_min_value = min(d.keys(), key=lambda k: d[k])
print(f'最小のValueを持つKey : {key_with_min_value}')
