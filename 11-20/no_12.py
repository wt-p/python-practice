# 自分の回答
height = float(input("身長を入力してください(cm) >"))
weight = float(input("体重を入力してください(kg) >"))
print(f"BMI = {weight / (height/100)**2}")

# 回答
h = float(input("身長を入力してください(cm) >")) / 100
w = float(input("体重を入力してください(kg) >"))

bmi = w / h**2
print(f"BMI = {bmi}")
