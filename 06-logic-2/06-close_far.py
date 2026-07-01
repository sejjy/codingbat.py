# Given three ints, a b c, return True if one of b or c is "close" (differing
# from a by at most 1), while the other is "far", differing from both other
# values by 2 or more. Note: abs(num) computes the absolute value of a number.
#
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True


def close_far(a, b, c):
  ab = abs(a - b)
  ac = abs(a - c)
  bc = abs(b - c)

  return (ab <= 1 and ac >= 2 and bc >= 2) or (ac <= 1 and ab >= 2 and bc >= 2)

  # close_far(8, 6, 9)
  #
  # ab = 2
  # ac = 1
  # bc = 3
  #
  # return (2 <= 1 and 1 >= 2 and 3 >= 2) or (1 <= 1 and 2 >= 2 and 3 >= 2)
  #            x          x         /     or     /          /         /
