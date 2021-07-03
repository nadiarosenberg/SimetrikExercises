import re

keylog = [
  '319',
  '680',
  '180',
  '690',
  '129',
  '620',
  '762',
  '689',
  '762',
  '318',
  '368',
  '710',
  '720',
  '710',
  '629',
  '168',
  '160',
  '689',
  '716',
  '731',
  '736',
  '729',
  '316',
  '729',
  '729',
  '710',
  '769',
  '290',
  '719',
  '680',
  '162',
  '289',
  '162',
  '718',
  '729',
  '319',
  '790',
  '680',
  '890',
  '362',
  '319',
  '760',
  '316',
  '729',
  '380',
  '319',
  '728',
  '716',
  '318',
  '389'
]

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

print('Password: ', password)

password = str(password)
if (len(password) == minimum_theoretical_length):
  print('Password has minimum length')

contains_everything = True
for value in keylog:
  for i in value:
    if i not in password: 
      contains_everything = False

if (contains_everything == True):
  print('Password is verified')
else:
  print('Password is wrong')









