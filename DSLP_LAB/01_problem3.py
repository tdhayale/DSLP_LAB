
list1=list(map(int,input("Enter first lists:").split())) 

list2=list(map(int,input("Enter second lists:").split()))

intersection =[]

for i in list1:
    if i in list2 and i not in intersection :
        intersection.append(i)
        
print("Intersection of two lists is =",intersection)