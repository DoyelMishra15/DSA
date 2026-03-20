def rec(s,n):
  if n==0:
    return
  rec(s,n-1)
  print(s)
rec("Doyel",5)
