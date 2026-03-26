#find the peak element

arr=list(map(int,input().split(',')))
n=len(arr)
for i in range(n):
  if (i==0 or arr[i-1] < arr[i]) and (i==n-1 or arr[i]>arr[i+1]):
    print(i)
    break
else:
  print(-1)
  
