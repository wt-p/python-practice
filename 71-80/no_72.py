# 自分の回答
d = {'A': 111, 'B': 222, 'C': 333}
l = ['B', 'C', 'D', 'A']
print(f'Bに対応するValue : {d.get(l[0])}')
print(f'Cに対応するValue : {d.get(l[1])}')
print(f'Dに対応するValue : {d.get(l[2])}')
print(f'Aに対応するValue : {d.get(l[3])}')

# 回答
d = {'A': 111, 'B': 222, 'C': 333}
l = ['B', 'C', 'D', 'A']
for key in l:
    print(f'{key}に対応するValue : {d.get(key)}')
