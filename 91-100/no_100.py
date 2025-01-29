# 自分の回答
normal_method = [method for method in dir([]) if not method.startswith('__')]
print(f'リストで使えるメソッド一覧 :\n {normal_method}')

# 回答
methods = dir(str)
non_special_methods = [s for s in dir(methods) if '__' not in s]
print(f'リストで使えるメソッド一覧 :\n {non_special_methods}')
