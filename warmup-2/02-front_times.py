def front_times(str, n):
  front = str[:3]
  result = ''
  for i in range(n):
    result += front
  return result


# Solution:

# def front_times(str, n):
#   front_len = 3
#   if front_len > len(str):
#     front_len = len(str)
#   front = str[:front_len]
#
#   result = ""
#   for i in range(n):
#     result = result + front
#   return result
