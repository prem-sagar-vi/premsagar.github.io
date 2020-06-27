fname=input('Enter file name:')
fhand=open(fname)
for line in fhand:
    line=line.strip()
    if line.startswith('From'):
        if not line.startswith('From:'):
            words=line.split()
            print(words[1])
        