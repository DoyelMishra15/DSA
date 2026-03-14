#Find the two numbers appearing odd number of times

nums = [1, 2, 1, 3, 5, 2]
xor=0
for i in nums:
  xor^=i 
xor1,xor2=0,0
for i in nums:
  if xor&1==1:
    xor2^=i 
  else:
    xor1^=i
  xor=xor>>1
print([xor1,xor2] if xor2>xor1 else [xor2,xor1])
