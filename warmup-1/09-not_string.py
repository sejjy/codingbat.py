def not_string(str):
  if not str[0:3] == "not":
    return "not " + str
  return str

# Solution:

# def not_string(str):
#   if len(str) >= 3 and str[:3] == "not":
#     return str
#   return "not " + str
#   # str[:3] goes from the start of the string up to but not
#   # including index 3
