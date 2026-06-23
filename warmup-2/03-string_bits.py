def string_bits(str):
  new_str = ""
  for i in range(len(str)):
    if i % 2 == 0:
      new_str += str[i]
  return new_str

# Solution:

# def string_bits(str):
#   result = ""
#   # Many ways to do this. This uses the standard loop of i on every char,
#   # and inside the loop skips the odd index values.
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result
