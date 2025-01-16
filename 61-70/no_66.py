# 自分の回答
d1 = {'A': 111, 'B': 222, 'C': 333}
d2 = {'D': 444, 'E': 555}
d3 = {'F': 666}
d4 = {}
for k, v in d1.items():
    d4[k] = v
for k, v in d2.items():
    d4[k] = v
for k, v in d3.items():
    d4[k] = v
print(f'連携した辞書 : {d4}')

# 回答
d1 = {'A': 111, 'B': 222, 'C': 333}
d2 = {'D': 444, 'E': 555}
d3 = {'F': 666}

new_d = {}
for d in [d1, d2, d3]:
    new_d.update(d)

print(f'連携した辞書 : {new_d}')
