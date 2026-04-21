s = input()
k = int(input())

def atMost(k):
    d = {}
    l = 0
    cnt = 0

    for r in range(len(s)):
        d[s[r]] = d.get(s[r], 0) + 1

        while len(d) > k:
            d[s[l]] -= 1
            if d[s[l]] == 0:
                del d[s[l]]
            l += 1

        cnt += (r - l + 1)

    return cnt

print(atMost(k) - atMost(k-1))
