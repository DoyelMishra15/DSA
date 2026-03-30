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
  left = max(weights)
  right = sum(weights)
  for capacity in range(left, right + 1):
    if daysNeeded(weights, capacity) <= d:
      return capacity
  return right


n=int(input())
weights=list(map(int,input().split()))
d=int(input())
print(shipWithinDays(weights, d))
