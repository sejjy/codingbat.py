def string_splosion(str):
  new_str = ""
  for i in range(len(str)):
    new_str += str[:i+1]
  return new_str

  # Solution:
  # result = ""
  # On each iteration, add the substring of the chars 0..i
  # for i in range(len(str)):
  #   result = result + str[:i+1]
  # return result
