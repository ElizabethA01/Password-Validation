# PASSWORD VALIDATION PROJECT EXERCISE
# SHORT ANSWER
import re 

pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$%#])[A-Za-z\d@$%#]{7,}")

# while True:
#   password = input('Insert a password: ')
#   if re.fullmatch(pattern, password):
#     print('Correct!')
#     break
#   else:
#     print('Try again')
#     continue

# MORE DETAILED
import re

lower = re.compile('[a-z]+')
upper = re.compile('[A-Z]+')
number = re.compile('\d+')
symbol = re.compile('[@$%#]+')

while True:
  password = input('Insert a password: ')
  if len(password) < 8:
    print('Password needs to more than 8 characters')
  if not re.search(lower, password):
    print('Lower case character is missing')
  if not re.search(upper, password):
    print('Upper case character is missing')
  if not re.search(number, password):
    print('Number is missing')
  if not re.search(symbol, password):
    print('Please use one of the following symbols: @, $, %, #')
  else:
    print('Valid password.')
    break
