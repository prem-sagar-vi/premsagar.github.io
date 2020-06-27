fname=input('Enter file name:')
fhand=open(fname)
count=dict()
lst=list()
for line in fhand:
    if line.startswith('From'):
        if not line.startswith('From:'):
            line=line.split()
            word=line[5].split(':')
            lst.append(word[0])
for w in lst:
    count[w]=count.get(w,0)+1
for k,v in sorted(count.items()):
    print(k,v)