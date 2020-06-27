fhand=open('romeo.txt')
lst=list()
for line in fhand:
    line=line.rstrip()
    word=line.split()
    for i in range(len(word)):
        if word[i] not in lst:
            lst.append(word[i])
lst.sort()
print(lst)
    