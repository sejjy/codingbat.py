def diff21(n):
  abs_diff = abs(n - 21)

  if n > 21:
    abs_diff *= 2
  return abs_diff

# Solution:

# def diff21(n):
#   if n <= 21:
#     return 21 - n
#   else:
#     return (n - 21) * 2
