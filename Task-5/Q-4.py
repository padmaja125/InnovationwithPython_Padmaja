def verify_pin(pin,real):
    if pin == real :
        return True
    else:
        return False

def log_in():
    user_name = input('Enter the username :')
    real = input('Enter password : ')
    tries = 0
    try:
        while tries < 3:
            pin = input('Re-Type password to confirm: ')
            if verify_pin(pin,real):
                print("Pin accepted!")
                return True
            else:
                print("Invalid pin")
                tries += 1
        raise ValueError
    except ValueError as ve:
        print(ve, "To many incorrect tries. try again later")
    return False

log_in()


# for default pin 
count = 0
while count < 3:
    user_name = input('Please enter your user name: ')
    password = input('PLease enter your password: ')

    if user_name != 'padma' or password != 'd@mr12':
        print('Wrong user name or password. Please try again.')

    else:
        print('Welcome to Banking')
        break
    count += 1
    
# method-2
username = "padmaja"
password = "d@mr12"
count = 0
while count < 3:
    username_input = input("enter a username")
    password_input = input("enter a password")
    if username_input == username and password_input == password:
        print("login success")
        count = 3
    else:
        print("Access denied, please reenter")
        count += 1
