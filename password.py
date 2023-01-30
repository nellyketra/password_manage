from cryptography.fernet import Fernet

'''def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb")as key_file:
        key_file.write(key)

write_key()'''

def load_key():
    file = open("key.key","rb")
    key=file.read()
    file.close()
    return  key



def view():
    with open ('pass.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user: ",user, ",| password: ",fer.decrypt(passw.encode()).decode())

def add():
    name= input("Account name: ")
    pwd= input("Password: ")

    with open ('pass.txt','a') as f:
        f.write(name+"|"+ fer.encrypt(pwd.encode()).decode()+ "\n")


master_password =input ("what is the master password?: ").lower()
key= load_key()
fer=Fernet(key)

if master_password=="mwagale":
    print('LET US START!!!')
    while True:
        mode=input("would you like to add a new pasword or view the existing ones'view'or'add'or'Q' to quit ?: ").lower()
        if mode=='q':
            break
        if mode=="view":
            view()
        elif mode=="add":
            add()
        else:
            print("invalid mode.")
            continue
else:
    quit()