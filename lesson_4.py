#дз 4.1
a=input()
mx=0
mxn=0
for i in range(len(a)):
  if a[i]=='н':
    mx+=1
  else:
    if mx>mxn:
      mxn=mx
    mx=0
a=a.replace('н','!')
print(a, mxn)
#дз 4.2
a='{[('
b=')}]'
c=input()
wr=False
s=''
for i in range(len(c)):
  if c[i] in b:
    wr=False
  if wr==True:
    s+=c[i]
  if c[i] in a:
    wr=True
print(s)
#дз 4.3
a=input()
m=[a for a in a.split()]
for i in m:
  if i[0]=='а' and i[-1]=='я':
    print(i)
