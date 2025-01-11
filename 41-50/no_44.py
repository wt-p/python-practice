# 自分の回答
l = [1, 2, 3, '4', 5]
re = ''
for v in l:
    if isinstance(v, str):
        re = 'str'
if re:
    print('文字列が入っています。')
else:
    print('文字列は入っていません。')

# 回答
l = [1, 2, 3, '4', 5]
if any(isinstance(v, str) for v in l):
    print('文字列が入っています。')
else:
    print('文字列は入っていません。')
