fname=input('Enter file name:')
fhand=open(fname)
word=dict()
for line in fhand:
    line=line.split()
    print(line)
    for x in line:
        word[x]=word.get(x,0)+1
print(word)