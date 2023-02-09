'''
Please make two below tasks in three calendar days.
Send us your solutions (even if not complete) in one file.
Each fix/improvement is additional point.

TASK 1.
Fix function shorten:
a) limit `10` should be variable and output should be less then limit
b) now function returns 12 chars for long strings (2 chars above limit)
c) delimiter `->` should be variable `...`
d) text "a          " should return "a"
e) other improvements

```
def shorten(text:str): -> str
  if len(text) => 10:
    return f'{text[:10]}->'
  else:
    return text
```

TASK 2.
Fix function validate:
a) output should return all errors with messages
b) if name contains only space there is no error
c) email "example.com" now is valid
d) password should check if there is:
- at least 2 uppercase chars
- at least 2 lowercase chars
- at least 4 digits
e) other improvements

```
def validate(form: dict): -> bool
  if not form.get('name'):
    return False
  if not form.get('email'):
    return False
  if not form.get('password'):
    return False
```
'''

import re

def shorten_improved(text):

    limit = 10
    delimiter = '...'

    if len(text.strip()) <= limit:
        return text.strip()
  
    else:
        return f'{text.strip()[:limit-len(delimiter)]}{delimiter}'
  

#TESTS:
'''
print(shorten_improved('Poszła Ola do przedszkola'))
print(shorten_improved('1234567891'))
print(shorten_improved('Natrętny'))
print(shorten_improved('cegla'))
print(shorten_improved('papier     '))
print(shorten_improved('      kamien7675666           '))
print(shorten_improved('         111111114343'))
'''
  

def validate_improved(form: dict):
    errors = []
    name = form.get('name').strip()
    email = form.get('email')
    password = form.get('password')

    if not name:
        errors.append("You forgot to enter name or it contains only spaces.")

    if not email:
        errors.append("You forgot to enter email address")

    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        errors.append("Wrong email format")

    if not password:
        errors.append("You forgot to enter password")

    elif not re.match(r'^(?=.*[A-Z].*[A-Z])(?=.*[a-z].*[a-z])(?=.*\d.*\d.*\d.*\d).{8,}$', password):
        errors.append("Password has to have at least 2 uppercase characters, 2 lowercase characters and 4 digits, and has to be 8 characters or more")

    if errors:
        return "\n".join(errors)
    else:
        return True

#TESTS:
'''

form = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'password': '1PASS$@word123'
}

form1 = {
    'name': '          ',
    'email': 'john.doe@example.com',
    'password': '1PASS$@word123'
}

form2 = {
    'name': 'John Doe',
    'email': '@joample.com',
    'password': '1PASS$@word153'
}
form3 = {
    'name': 'John Doe',
    'email': 'joexa@mple.com',
    'password': 'P2222223'
}

form4 = {
    'name': '          ',
    'email': '           ',
    'password': '        '
}
form5 = {
    'name': '',
    'email': '',
    'password': ''
}

print(validate_improved(form))
print('-----------------------------------------')
print(validate_improved(form1))
print('-----------------------------------------')
print(validate_improved(form2))
print('-----------------------------------------')
print(validate_improved(form3))
print('-----------------------------------------')
print(validate_improved(form4))
print('-----------------------------------------')
print(validate_improved(form5))
print('-----------------------------------------')

'''