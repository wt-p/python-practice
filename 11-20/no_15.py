# 自分の回答
num1 = int(input("1つ目の整数を入力してください >"))
num2 = int(input("2つ目の整数を入力してください >"))
res = num1 - num2
if res < 0:
    print(f"計算結果 : {-res}")
else:
    print(f"計算結果 : {res}")

# 回答
a = int(input('1つ目の整数を入力してください > '))
b = int(input('2つ目の整数を入力してください > '))
r = a - b
r = -r if r < 0 else r
print(f'計算結果 : {r}')
