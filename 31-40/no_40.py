# 自分の回答
l = [1, '22', 3, '444', 0.0, '5']
new_l = [i for i in l if isinstance(i, int)]
print(f"最大値 : {max(new_l)}")
print(f"最小値 : {min(new_l)}")

# 回答
l = [1, '22', 3, '444', 0.0, '5']
new_l = [v for v in l if isinstance(v, int)]
print(f'最大値 : {max(new_l)}')
print(f'最小値 : {min(new_l)}')