word = input().split()
anagram = {}
for ele in word:
    std = ''.join(sorted(ele))
    if std in anagram:
        anagram[std].append(ele)
    else:
        anagram[std] = [ele]
res = list(anagram.values())
print(res)        