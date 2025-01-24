# 自分の回答
l = [1, 2, None, False, '3', '4', None, True]
new_l1 = []
new_l2 = []
for v in l:
    if isinstance(v, bool):
        new_l1.append(v)
    if v is None:
        new_l2.append(v)
print(f'TrueとNoneの数 : {sum(new_l1) + len(new_l2)}')

# 回答
l = [1, 2, None, False, '3', '4', None, True]
is_true_or_none = [v for v in l if v is True or v is None]
print(f'TrueとNoneの数 : {len(is_true_or_none)}')
