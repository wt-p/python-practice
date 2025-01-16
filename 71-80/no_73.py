# 自分の回答
d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
sorted_l = sorted(d.items(), key=lambda x: x[0])
new_d = {k: v for k, v in sorted_l}
print(f'Keyでソートした辞書 : {new_d}')

# 回答
d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
sort_by_key = dict(sorted(d.items()))
print(f'keyでソートした辞書 : {sort_by_key}')
