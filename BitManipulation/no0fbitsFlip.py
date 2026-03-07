//Count number of bits to be flipped to convert A to B

n=int(input())
m=int(input())
xor=n^m
count = 0
while xor:
  x=xor&1 
  if x==1:
    count+=1 
  xor=xor>>1 
print(count)
