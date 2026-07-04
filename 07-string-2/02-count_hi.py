# Return the number of times that the string "hi" appears anywhere in the given
# string.
#
# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2


def count_hi(str):
  count = 0

  # fmt: off
  for i in range(len(str)-1):
    if (str[i] + str[i+1]) == 'hi':
      count += 1
  # fmt: on

  return count


# Solution:

# def count_hi(str):
#   sum = 0
#   ## Loop to length-1 and access index i and i+1
#   ## in the loop.
#   for i in range(len(str)-1):
#     if str[i:i+2] == 'hi':
#       sum = sum + 1
#   return sum
