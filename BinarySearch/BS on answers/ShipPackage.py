#Capacity to Ship Packages within D Days

def daysNeeded(weights, capacity):
    days = 1
    currentLoad = 0
    for w in weights:
        if currentLoad + w > capacity:
            days += 1
            currentLoad = w
        else:
            currentLoad += w
    return days


def shipWithinDays(weights, d):
    l = max(weights)
    r = sum(weights)
    while l < r:
        mid = (l + r) // 2
        if daysNeeded(weights, mid) <= d:
            r = mid
        else:
            l = mid + 1
    return l


n=int(input())
weights=list(map(int,input().split()))
d=int(input())
print(shipWithinDays(weights, d))
