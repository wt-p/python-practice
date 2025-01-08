# 自分の回答
l1 = [1 ,2 ,3, 4, 5]
l2 = [10, 9, 8, 7, 6]
new_l = [l1[i]*l2[i] for i in range(len(l1))]
print(f"掛け算を計算した結果 : {new_l}")

# 回答
l1 = [1 ,2 ,3, 4, 5]
l2 = [10, 9, 8, 7, 6]
l3 = [i * j for i, j in zip(l1, l2)]
print(f'掛け算を計算した結果 : {l3}')