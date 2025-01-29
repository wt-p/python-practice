# 自分の回答
import re
l = ['アメリカ', 'カナダ', 'スイス', 'メキシコ', 'セントルシア', 'タイ']
s = ['サ', 'シ', 'ス', 'セ', 'ソ']
new_l = [v for v in l if re.search('[サ-ソ]', v)]
print('サ行を含む単語 :')
for v in new_l:
    print(v)

# 回答
l = ['アメリカ', 'カナダ', 'スイス', 'メキシコ', 'セントルシア', 'タイ']
sa_l = ['サ', 'シ', 'ス', 'セ', 'ソ']

print('サ行を含む単語:')
for word in l:
    for sa in sa_l:
        if sa in word:
            print(word)
            break
