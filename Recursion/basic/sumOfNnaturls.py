#Sum of first N Natural Numbers

def sm(n):
  if n==1:
    return 1 
  return n+sm(n-1)
print(sm(3))
