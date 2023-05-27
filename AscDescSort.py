n = int(input("Enter the number of list:- "))
list=[]
asc=[]
dec=[]
for i in range(n):
    list.append(int(input("Enter the list Element :- ")))

asc = sorted(list)
dec = sorted(list, reverse=True)

print("Ascending", asc)
print("Decending", dec)