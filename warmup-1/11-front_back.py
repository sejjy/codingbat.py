def front_back(str):
  first = str[:1]
  last = str[-1:]
  
  if first == last:
    return str
  return (last + str[1:len(str)-1] + first)

  # Solution:
  # if len(str) <= 1:
  #   return str
  #
  # mid = str[1:len(str)-1]  # can be written as str[1:-1]

  # last + mid + first
  # return str[len(str)-1] + mid + str[0]
