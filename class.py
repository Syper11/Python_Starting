age = int(input("What is your age?" ))

if age < 18:
    print('kids')
elif age <= 65:
    print('adults')
else:
    print('seniors')