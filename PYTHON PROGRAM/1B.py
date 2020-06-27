fname=input('Enter file name:')
fhand=open(fname)
count=0
s=0.0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        x1=line[19:]
        x1=x1.rstrip()
        x=float(x1)
        s=x+s
avg=s/count
print(avg)