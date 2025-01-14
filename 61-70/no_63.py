# 自分の回答
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5]
s1 = set(l1) & set(l2)
boolean1 = True
boolean2 = True
if list(s1) == l1 :
    booolean1 = True
else:
    boolean1 = False
if list(s1) == l2:
    boolean2 = True
else:
    boolean2 = False
print(f'l1はl2に含まれている : {boolean1}')
print(f'l2はl1に含まれている : {boolean2}')

# 回答
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5]

print(f'l1はl2に含まれている : {set(l1).issubset(set(l2))}')
print(f'l2はl1に含まれている : {set(l2).issubset(set(l1))}')