# 自分の回答
l1 = [4, 6, 9, 2]
l2 = [3, 5, 7]
l3 = [1, 9, 7]
l1_average = sum(l1) / len(l1)
l2_average = sum(l2) / len(l2)
l3_average = sum(l3) / len(l3)

print(f'平均値が最も高いリスト : ')

# 回答
l1 = [4, 6, 9, 2]
l2 = [3, 5, 7]
l3 = [1, 9, 7]

# 1つのリストに格納する
l = [l1, l2, l3]
# 各リストの平均値を計算してソートする
sorted_l = sorted(l, key=lambda v: sum(v) / len(v), reverse=True)
# ソートしたリストからインデックス番号0番目を取得する
print(f'平均値が最も高いリスト : {sorted_l[0]}')