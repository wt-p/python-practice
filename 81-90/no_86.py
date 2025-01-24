# 自分の回答
l = [1, 2, None, 3]
for i in l:
    if i is None:
        print(10000)
    else:
        print(i)

# 回答
l = [1, 2, None, 3]

for v in l:
    if v is None:
        v = 10000
    print(v)
