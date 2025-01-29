# 自分の回答
s = 'This is the Python exercise.'
l = s.split()
new_l = [v for v in l if 't' not in v]
new_s = ' '.join(new_l)
print(f'削除後の文字列 : {new_s}')

# 回答
s = 'This is the Python exercise.'
l = [v for v in s.split() if 't' not in v]

new_s = ' '.join(l)
print(f'削除後の文字列 : {new_s}')
