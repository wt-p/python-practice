# 自分の回答
l = [1, 2, 3, 3]
x = len(l)
y = len(set(l))
if x == y:
    print('重複する値がありません。')
else:
    print('重複している値があります。')

# 回答
l = [1, 2, 3, 3]
if len(set(l)) < len(l):
        print('重複している値があります。')
else:
    print('重複する値がありません。')