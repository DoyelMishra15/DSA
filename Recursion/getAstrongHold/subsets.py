#subsets

s=input()
n=len(s)
for i in range(1<<n):
  sub=''
  for j in range(n):
    if (i>>j)&1==1:
      sub+= s[j]
  print(sub)
