name = input("What's your name? ")

age = int(input('How old are you? '))

if name == 'Ola' or 'Ania' or 'Justyna' or 'Marta':
    print(f'Hello {name}')
if name == 'Ola' and age > 17:
    print(f'Hello {name}. You''\'re an adult')

elif age < 17 :
    print('You''\'re not old enough')
else:
    print('You cannot use this')
