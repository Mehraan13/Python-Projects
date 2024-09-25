master_pwd = input("Enter Master Password: ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #rstrip is used to get rid of the \n read in
            user, pas = data.split(' | ')
            print(f"User: {user} and Pass: {pas}")
def add():
    name = input("Account Name: ")
    pwd = input('Password: ')
    #open file using with (automatically closes) in append mode
    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + pwd + ' \n')
        



#main body
while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add, quit) ").lower()

    if mode == "quit":
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid option.")
        continue


print("Program Terminated. ")