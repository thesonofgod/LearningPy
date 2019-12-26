while True:
    print('Who are You?')
    name = input()
    if name != 'Prashanth':
        continue
    print('Hello, Prashanth. What is the Password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')