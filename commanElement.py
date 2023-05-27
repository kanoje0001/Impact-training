n1 = int(input("Enter the list1 number : "))
n2 = int(input("Enter the list2 number : "))
list1 = []
list2 = []
list3 = []
for i in range(n1):
    list1.append(input("Entr list1 :"))
for i in range(n2):
    list2.append(input("Entr list2 :"))    
for i in range(n1):
    for j in range(n2):
        if list1[i]==list2[j] and list1[i] not in list3:
            list3.append(list[i])
    print(list3)            