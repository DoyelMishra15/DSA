def myAtoi(s):
  s = s.lstrip()
  if not s:
    return 0

  sign = 1
  i = 0

  if s[0] == '-':
    sign = -1
    i += 1
  elif s[0] == '+':
    i += 1

  INT_MIN = -2147483648
  INT_MAX = 2147483647

  def solve(i, num):
    if i >= len(s) or not s[i].isdigit():
      return num

    num = num * 10 + int(s[i])

    if sign * num <= INT_MIN:
      return abs(INT_MIN)
    if sign * num >= INT_MAX:
      return INT_MAX

    return solve(i + 1, num)

  ans = solve(i, 0) * sign

  if ans < INT_MIN:
    return INT_MIN
  if ans > INT_MAX:
    return INT_MAX

  return ans


s = input()
print(myAtoi(s))
