#Print Prime Factors of a Number
n = int(input())
t = n
l = []

i = 2
while i * i <= t:
    if t % i == 0:
        l.append(i)
        while t % i == 0:
            t //= i
    i += 1

if t != 1:
    l.append(t)

print(l)
