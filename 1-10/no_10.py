# 自分の回答
import re
list = []
for i in range(1, 41):
    if i % 3 == 0 and re.search('3', str(i)):
        list.append(i)
print(f"作成したリスト:{list}")

# 回答
list = []
for i in range(1, 41):
    if i % 3 == 0 and '3' in str(i):
        list.append(i)
print(f"作成したリスト:{list}")
