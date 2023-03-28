import mysql.connector as mysql

db=mysql.connect(host='localhost',user='root', password='',database='college_management')
command_handler=db.cursor(buffered=True)

def admin_session():
    while 1:
        print('')
        print('Admin menu:')
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete existing Student")
        print("4. Delete existing Teacher")
        print("5. Log out")

        user_option=input('Option: ')

        if user_option=='1':
            print("")
            print("Register new Student")
            username=input("Student username: ")
            password=input("Student password: ")
            query_vals=(username, password)
            command_handler.execute("INSERT INTO users (username,password,priviledge) VALUES (%s, %s, 'student')",query_vals)
            db.commit()
            print(username + 'has been registered as a student')

        elif user_option=='2':
            print("")
            print("Register new Teacher")
            username=input("Teacher username: ")
            password=input("Teacher password: ")
            query_vals=(username, password)
            command_handler.execute("INSERT INTO users (username,password,priviledge) VALUES (%s, %s, 'teacher')",query_vals)
            db.commit()
            print(username + 'has been registered as a teacher')

        elif user_option=='3':
            print("")
            print("Delete existing Student Account")
            username=input("Student username: ")
            query_vals=(username, 'student')
            command_handler.execute("DELETE FROM users WHERE username=%s AND priviledge=%s",query_vals)
            db.commit()
            if command_handler.rowcount<1:
                print("User not found")
            else:
                print(username + 'has been deleted')

        elif user_option=='4':
            print("")
            print("Delete existing Teacher Account")
            username=input("Teacher username: ")
            query_vals=(username, 'teacher')
            command_handler.execute("DELETE FROM users WHERE username=%s AND priviledge=%s",query_vals)
            db.commit()
            if command_handler.rowcount<1:
                print("User not found")
            else:
                print(username + 'has been deleted')

        elif user_option=='5':
            break

        else:
            print("Not a valid option")

def auth_admin():
    print("")
    print("Admin login")
    print("")
    username=input("Username: ")
    password=input("Password: ")
    if username=='janvi':
        if password=='1234':
            admin_session()
        else:
            print("Incorrect credentials")

    else:
        print("login details not recognised")

    
def main():
    while 1:
        print("Welcome to the college system")
        print("")
        print("1. Login as Student")
        print("2. Login as Teacher")
        print("3. Login as Admin")

        user_option=input("option: ")
        if user_option=='1':
            print("Student login")
        elif user_option=='2':
            print("Teacher login")
        elif user_option=='3':
            auth_admin()
        elif user_option=='4':
            break
        else:
            print("Not a valid choice")
main()