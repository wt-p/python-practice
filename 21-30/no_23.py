# 自分の回答
first_char = input("1つ目の英文を入力してください >").split(" ")
second_char = input("2つ目の英文を入力してください >").split(" ")
result = [a for a in first_char if a in second_char]
print(f"重複する英単語 : {result}")

# 回答
sentence1 = input("1つ目の英文を入力してください >")
sentence2 = input("2つ目の英文を入力してください >")

sentence1 = sentence1.split()
sentence2 = sentence2.split()

r = []
for word in sentence1:
    if word in sentence2 and word not in r:
        r.append(word)
print(f"重複する英単語 : {r}")