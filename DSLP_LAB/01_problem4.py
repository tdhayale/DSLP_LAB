words =["Ram","Tejas ","Hitesh","Shubham","Tejas","Tejas","Tejas","Shubham"]

given_word=input("Enter word:")

occ=int(input("Enter occurence to remove:"))
count=0
for i in words:
    if i==given_word:
        count+=1

        if count == occ:
            words.remove(i)
            break

print(words)