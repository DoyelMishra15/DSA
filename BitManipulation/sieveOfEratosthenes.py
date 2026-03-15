l, r = map(int, input().split())

isprime = [True] * (r + 1)
isprime[0], isprime[1] = False, False

p = 2
while p * p <= r:
  if isprime[p]:
    for i in range(p * p, r + 1, p):
      isprime[i] = False
  p += 1

primeCount = [0] * (r + 1)

for i in range(1, r + 1):
  primeCount[i] = primeCount[i - 1]
  if isprime[i]:
    primeCount[i] += 1

print(primeCount[r] - primeCount[l - 1])
