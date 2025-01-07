# 自分の回答
# first = input("1つ目の英単語を入力してください >")
# second = input("2つ目の英単語を入力してください >")
# third = input("3つ目の英単語を入力してください >")
# l = sorted([first, second, third])
# result = ", ".join(l)
# print(f"並び替えた英単語 : {result}")

# 回答
word1 = input("1つ目の英単語を入力してください >")
word2 = input("2つ目の英単語を入力してください >")
word3 = input("3つ目の英単語を入力してください >")
words = [word1, word2, word3]
# print(words)
words.sort()
# print(words)
sort_words = ", ".join(words)

print(f"並び替えた英単語 : {sort_words}")