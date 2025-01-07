# 自分の回答
l = ['Python', 'Ruby', 'PHP', 'JavaScript']
min_char = min(l, key=len)
print(f"一番短い単語 : {min_char}")

# 回答
l = ['Python', 'Ruby', 'PHP', 'JavaScript']

min_length_word = l[0]

for word in l[1:]:
    min_length = len(min_length_word)
    if len(word) < min_length:
        min_length_word = word

print(f"一番短い単語 : {min_length_word}")

# 別解
l = ['Python', 'Ruby', 'PHP', 'JavaScript']
sorted_l = sorted(l, key=len)
print(f"一番短い単語 : {sorted_l[0]}")