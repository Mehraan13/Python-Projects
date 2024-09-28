from cryptography.fernet import Fernet #module that allows us to encrypt text

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    f = open("key.key", "rb")
    key = f.read()
    f.close() #closing file to avoid errors
    return key


master_pwd = input("Enter Master Password: ")

while True:
    if master_pwd == 'pass@123':
        break
    else:
        print("Wrong Pass")
        quit()

key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #rstrip is used to get rid of the \n read in
            user, pas = data.split(' | ')
            dec_pas = fer.decrypt(pas.encode()).decode()
            print(f"User: {user} and Pass: {dec_pas}")

def add():
    name = input("Account Name: ")
    pwd = input('Password: ')
    #open file using with (automatically closes) in append mode
    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + fer.encrypt(pwd.encode()).decode() + ' \n')
        



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