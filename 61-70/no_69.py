# 自分の回答
d = {'A': 111, 'B': 222, 'C': 333}
VALUE = 444
result = False

for k, v in d.items():
    if v == VALUE:
        result = True

print(f'444は辞書に含まれているか : {result}')

# 回答
d = {'A': 111, 'B': 222, 'C': 333}
result = 444 in d.values()
print(f'444は辞書に含まれているか : {result}')
