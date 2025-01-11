# 自分の回答
l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
new_l = []
for v in l:
    if 'Python' not in str(v):
        new_l.append(v)
print(f'文字列"Python"を削除したリスト : {new_l}')

# 回答1
l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
for v in l:
    if 'Python' in str(v):
        l.remove(v)
print(f'文字列"Python"を削除したリスト : {l}')

# 回答2
l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
new_l = [v for v in l if 'Python' not in str(v)]
print(f'文字列"Python"を削除したリスト : {new_l}')