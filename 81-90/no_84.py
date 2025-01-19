# 自分の回答
l = [1, 0, [], (2, 3), 'AA', '', False, ''*3]
new_l = [bool(b) for b in l]
print(f'Trueの数 : {new_l.count(True)}')

# 回答
l = [1, 0, [], (2, 3), 'AA', '', False, ''*3]
is_true_list = [bool(v) for v in l]
print(f'Trueの数 : {sum(is_true_list)}')

# 別解
l = [1, 0, [], (2, 3), 'AA', '', False, ''*3]
is_true_list = [v for v in l if v]
print(f'Trueの数 : {len(is_true_list)}')
