list1 = list(map(int,input("Enter elements of first list:").split()))

list2 = list(map(int,input("Enter elements of first list:").split()))

#union = list(set(list1)|set(list2))
#print("Union of two lists=",union)
union=[]
for i in list1:
     if i  not in union:

        union.append(i)

for j in list2: 
  if j not in union:
   union.append(j)

print("The union of two lists is=",union)
