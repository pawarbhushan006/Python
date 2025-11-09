import os

while True:
    if not os.path.exists('Output.txt'):
        Input_user=  input('Enter text to write to the file: ')
        with open('Output.txt','w') as f:
            f.write(f'{Input_user}\n')
            print('Data successfully written to Output.txt')
    else:
        choice = input('Would you like to continue? (y/n): ')
        if choice == 'y':
            Input_user = input('Enter additional text to append :')
            with open('Output.txt','a') as f:
                f.write(f'{Input_user}\n')
                print('Data successfully appended')
        else:
            break
print('final content of Output.txt:')
with open('Output.txt','r') as f:
    print(f.read())

