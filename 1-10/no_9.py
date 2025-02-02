# 自分の回答
num_dict = {}
num = 1
for i in range(1, 31):
    if i % 3 == 0:
        num_dict[f"{num}番目"] = i
        num += 1
print(f"作成した辞書{num_dict}")

# 回答
d = {}
for i in range(1, 31):
    if i % 3 == 0:
        index = f"{i // 3}番目"
        d[index] = i
print(f"作成した辞書: {d}")
