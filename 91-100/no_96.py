# 自分の回答
import ast
s = '{"A": 111, "B": 222, "C": 333}'
d = ast.literal_eval(s)
print(f'変換した辞書 : {d}')
print(f'型: {type(d)}')

# 回答
import json

s = '{"A": 111, "B": 222, "C": 333}'
d = json.loads(s)

print(f'変換した辞書 : {d}')
print(f'型: {type(d)}')
