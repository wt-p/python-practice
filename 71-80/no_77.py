# 自分の回答
d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
new_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(f'辞書に格納されているValueの最大値 : {new_d[0][1]}')

# 回答
d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
max_value = max(d.values())
print(f'辞書に格納されているValueの最大値 : {max_value}')
