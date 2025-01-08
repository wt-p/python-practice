# 自分の回答
l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
new_l = sum(l, [])
print(f"一次元にしたリスト : {new_l}")

# 回答
l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
new_l = [i for row in l for i in row]
print(f'一次元にしたリスト : {new_l}')