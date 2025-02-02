# 自分の回答
word = input("文字列を入力してください >")
dic = {}
print(word)
for s in word:
    if s in dic.keys():
        dic[s] += 1
    else:
        dic[s] = 1
print(dic)

# 回答
word = input('文字列を入力してください > ')

d = {}
for s in word:
    if s in d.keys():
        d[s] += 1
    else:
        d[s] = 1
print(d)
