import re

with open("keylog.txt", "r") as file:
  keylog = file.read().splitlines()

def get_password(keylog):
  all_numbers = []
  for value in keylog:
    all_numbers.append(value[0])
    all_numbers.append(value[1])
    all_numbers.append(value[2])
  all_numbers = set(all_numbers) 
  minimum_theoretical_length = len(all_numbers)

  password = 1
  for i in range(1,minimum_theoretical_length):
      password *= 10
      password += i+1
  solved = False
  while not solved:
      str_password = str(password)
      if set(str_password) == all_numbers:
          tested = 0
          for value in keylog:
              if not re.search(r"{0}.*{1}.*{2}".format(value[0],value[1],value[2]), str_password):
                  break
              tested += 1
          if tested == len(keylog):
              solved = True
              break
      password+=1

  return {"password": password, "minimum_theoretical_length": minimum_theoretical_length} 

def has_minimum_theoretical_length(minimum_theoretical_length, password):
  password = str(password)
  if (len(password) == minimum_theoretical_length):
    message = 'Password has minimum length'
  else:
    message = 'Password has not minimum length'
  return message

def is_valid_password(keylog, password):
  password = str(password)
  contains_everything = True
  for value in keylog:
    order = []
    for i in value:
      try:
        index_i = password.index(i)
        order.append(index_i)
      except:
        contains_everything = False
      asc_order = sorted(order)
      if not order == asc_order:
        contains_everything = False
  if (contains_everything == True):
    message = 'Password is verified'
  else:
    message = 'Password is wrong'
  return message

get_password = get_password(keylog)
password = get_password["password"]
minimum_theoretical_length = get_password["minimum_theoretical_length"]
print('Password: ', password)
print(has_minimum_theoretical_length(minimum_theoretical_length, password))
print(is_valid_password(keylog, password))






