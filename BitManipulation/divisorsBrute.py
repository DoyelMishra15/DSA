#Print all Divisors of a given Number

n=int(input())
def isprime(n):
  if n<=1:
      return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

for i in range(1,n+1):
  if isprime(i) and n%i==0:
    print(i,end=' ')
