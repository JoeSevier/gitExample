print('begin')
for attempt_number in range(3):
    username = input('Username: ')
    if username in ('bob', 'jane', 'sally', 'allan','arnold', 'jim', 'shasha'):
        print(f'Welcome {username}')
        break
    print('Invalid login: go away!')
    print("You have used ", (attempt_number+1), " of your 3 attempts.")
else:
    print(f'You tried 3 times. Now I hate you')
print('end')
