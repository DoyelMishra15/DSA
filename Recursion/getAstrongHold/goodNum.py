#Count Good numbers

#Problem Statement: A digit string is considered good if the digits at even indices (0-based) are even digits (0, 2, 4, 6, 8) and the digits at odd indices are prime digits (2, 3, 5, 7).

n=int(input())

# ans=1

# for i in range(n):
#   if i%2==0 :
#     ans = ans * 5
#   else:
#     ans=ans*4
# print(ans)

mod = 10**9 + 7
even = (n + 1) // 2
odd = n // 2
ans = (pow(5, even, mod) * pow(4, odd, mod)) % mod
print(ans)
