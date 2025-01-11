# 自分の回答
l = [1, 2, 3, 4, 5]
new_l = []
for i in l:
    new_l.append('list')
    new_l.append(i)
print(f'"list"を追加したリスト : {new_l}')

# 回答
l = [1, 2, 3, 4, 5]
for i in range(0, 10, 2):
    l.insert(i, 'list')
print(f'"list"を追加したリスト : {l}')