# 自分の回答
l = [4, 'aaa', 2, 'ddd', 'ccc', 3, 1, 'bbb']

new_l1 = []
new_l2 = []
new_l3 = []
for i in l:
    if isinstance(i, int):
        new_l1.append(i)
    else:
        new_l2.append(i)
new_l3 = sorted(new_l1) + sorted(new_l2)
print(f'ソートしたリスト : {new_l3}')

# 回答
l = [4, 'aaa', 2, 'ddd', 'ccc', 3, 1, 'bbb']
int_l = sorted([v for v in l if isinstance(v, int)])
str_l = sorted([v for v in l if isinstance(v, str)])
print(f'ソートしたリスト : {int_l + str_l}')