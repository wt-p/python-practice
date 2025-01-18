# 自分の回答
d = {'B': 222, 'A': 111, 'D': 333, 'C': 444}
sort_by_value = dict(sorted(d.items(), key=lambda x: x[1]))
print(f'Valueでソートした辞書 : {sort_by_value}')

# 回答
d = {'B': 222, 'A': 111, 'D': 333, 'C': 444}
sort_by_value = dict(sorted(d.items(), key=lambda x: x[1]))
print(f'Valueでソートした辞書 : {sort_by_value}')
