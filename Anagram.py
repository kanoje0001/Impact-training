n = int(input())
n2 = int(input())
list1 = []
list2 = []
for character in range(n):
    list1.append(input())
for charater in range(n2):
    list2.append(input())
list1.sort()
list2.sort()         
if list1 == list2:
    print("Anagram")
else:
    print("not anagram")
