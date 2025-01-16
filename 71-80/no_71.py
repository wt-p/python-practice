# 自分の回答
d = {'A': 111, 'B': 222, 'C': 333}
new_d = {}
for k, v in d.items():
    if v > 150:
        new_d.update({k: v})
print(f'絞り込みをかけた辞書 : {new_d}')

# 回答
d = {'A': 111, 'B': 222, 'C': 333}
new_d = {key:value for key, value in d.items() if value > 150}
print(f'絞り込みをかけた辞書 : {new_d}')
