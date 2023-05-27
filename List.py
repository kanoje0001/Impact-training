n1 = int(input("Enter the no.of first list of Number :="))
n2 = int(input("Enter the no.of second list of Number :="))
list1=[]
list2=[]
clist=[]
for i in range(n1):
    list1.append(input("Enter Element: "))
for i in range(n2):
    list2.append(input("Enter Element: "))

for i in range(n1):
    for j in range(n2):
        if list1[i]==list2[j] and list1[i] not in clist:
            clist.append(list1[i])
print(clist)            
                
