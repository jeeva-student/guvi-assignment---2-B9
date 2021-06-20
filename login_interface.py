import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="login_interface")
cur = con.cursor(buffered=True)

def Register():
    import re
    Name = input("enter the user_name or email id: ")
    re_name = input("re enter the user_name or email id: ")
    Password = input("enter the password: ")
    if Name == re_name:
        def check(email):

            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if (re.search(regex, email)):
                print("user saved")
            else:
                print("Invalid Email Enter the valid email with ""@"", "".""")

        if __name__ == '__main__':
            check(Name)
        cur.execute("""select user_name from login__interface where user_name =\"""" + Name + """\";""")
        result = cur.fetchone()
        if result != None:
            print("enter another username")
        else:
            password = Password
            flag = 0
            while True:
                if (len(password) >= 16):
                    flag = -1
                    break
                elif(len(password)<=5):
                    flag = -1
                    break
                elif not re.search("[a-z]", password):
                    flag = -1
                    break
                elif not re.search("[A-Z]", password):
                    flag = -1
                    break
                elif not re.search("[0-9]", password):
                    flag = -1
                    break
                elif not re.search("[_@$]", password):
                    flag = -1
                    break
                elif re.search("\s", password):
                    flag = -1
                    break
                else:
                    flag = 0
                    cur.execute("""INSERT INTO login__interface (user_name, password) VALUES (\"""" + Name + """\",\"""" + Password + """\")""")
                    con.commit()
                    break

            if flag == -1:
                print("Not a Valid Password")
                print("enter the valid password with minimum of 1.one lower case, 2.one upper case, 3.one number, 4.one special character")
    else:
        print("enter the same user_name or email id")





def Login():
    new = input("enter the user name: ")
    def check_name(name):
        import re
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, name)):
            print("verified")
        else:
            print("Invalid Email Enter the valid email with ""@"", "".""")
            quit()
    if __name__ == '__main__':
        check_name(new)

    cur.execute("""select user_name from login__interface where user_name =\"""" + new + """\";""")
    result = cur.fetchone()
    if result == None:
        print("enter the valid email id")
    else:
        for i in result:
            name = i
            break


    passw = input("enter the password: ")
    import re
    password = passw
    flag = 0
    while True:
        if (len(password) >= 16):
            flag = -1
            break
        elif(len(password)<=5):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            print("password verified")
            break

    if flag == -1:
        print("Not a Valid Password")
        print("enter the valid password with minimum of 1.one lower case, 2.one upper case, 3.one number, 4.one special character", end="\n")

    cur.execute("""select password from login__interface where password =\"""" + passw + """\";""")

    result = cur.fetchone()
    if result == None:
        print("enter the valid password")
        print("you want to register enter 1 to register, enter 2 to get the forgetten password, enter 3 for back to login, enter 4 for exit")
        a = int(input("enter the number: "))
        if a == 1:
            Register()
        elif a == 2:
            name1 = input("enter the username for getting the password: ")
            cur.execute("""select password from login__interface where user_name =\"""" + name1 + """\";""")
            result = cur.fetchone()
            for i in result:
                print("the forgotten password: ", i)
        elif a == 3:
            Login()
        elif a == 4:
            return

    elif result != None:
        for i in result:
            password = i
        print("login successful")



    else:
        return


while(True):
    print('Menu')
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    a = int(input("Enter the value: "))
    if a == 3:
        print(" ******** Thank you using our Application **********")
        break
    elif a == 1:
        Register()
    elif a == 2:
        Login()