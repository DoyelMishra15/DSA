#Divide two integers without using multiplication, division and mod operator
a, b = map(int, input().split())
cnt = 0
while a >= b:
    a = a - b
    cnt += 1
print(cnt)
