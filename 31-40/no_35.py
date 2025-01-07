# 自分の回答
l = ['1', 2, '3', 4.0, '5', 6, '7', 8.0, '9', 10]
int_list = []
for x in l:
    if type(x) == int:
        int_list.append(x)
print(f"正数型に絞り込んだリスト : {int_list}")

# 回答
l = ['1', 2, '3', 4.0, '5', 6, '7', 8.0, '9', 10]
new_l = []

for v in l:
    if isinstance(v, int):
        new_l.append(v)
print(f'正数型に絞り込んだリスト : {new_l}')