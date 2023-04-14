import sqlite3


def cursor():
    cnxn = sqlite3.connect("./login_device.db")
    return cnxn.cursor()


def update_user(username):
    cnxn = sqlite3.connect("./login_device.db")
    choice = input("Would you like to update your 1.username or 2.password? >>>: ")
    if choice == "1":
        new = input("what would you like to change your username to? >>>: ")
        query = f"UPDATE users SET username = {new} WHERE username = ?"
    elif choice == "2":
        newest = input("what would you like to change your password to? >>>: ")
        query = f"UPDATE users SET password = {newest} WHERE username = ?"


    cnxn.cursor().execute(query, (username,))
    cnxn.commit()
    cnxn.close()
    print("Your password/username has been changed succsefully")
    


# print(cursor.execute("select * from users").fetchall())
def delete():
    cnxn = sqlite3.connect("./login_device.db")
    user = input("What is the user you whant to delete? >>>: ")
    proceed = input(f"This is permanant! Delete {user}?(y,n) >>>: ")
    if proceed == "y":
        cnxn.cursor().execute("delete from users where username = ?", (user,))
        cnxn.commit()
        cnxn.close()


def search():
    for _ in range(100):
        user_username = input("What is the user's username >>>: ")
        all = cursor().execute("select * from users where username = ?", (user_username,)).fetchone()
        if not all:
            answer = input("username not found. Do you what to try agin?(y,n) >>>:")
            if answer == "n":
                break
        else:
            print(f"User id: {all[0]} | Username: {all[1]} | Password: {all[2]}")
            print("====================================================================\n")
            answer1 = input("Do you what to search agin?(y,n) >>>:")
            if answer1 == "n":
                break


def users_grabAll():
    all = cursor().execute("select * from users").fetchall()
    for user in all:
        print(f"User id: {user[0]} | Username: {user[1]} | Password: {user[2]}")
        print("====================================================================\n")



def user_options(username):
    for _ in range(20):
        selection = input("what would you like to do\n1.View all users\n2.Search users\n3.Delete user\n4.Update user\n>>>: ")
        if selection == "1":
            users_grabAll()
        elif selection == "2":
            search()
        elif selection == "3":
            delete()
        elif selection == "4":
            update_user(username)



def login():
    for _ in range(100):
        try:
            username = input("Please enter your username >>>: ")
            password = input("Please enter your password >>>: ")

            results = cursor().execute("select * from users where username = ?", (username,)).fetchone()
            if not results:
                return "Username not found"
            else:
                if password == results[2]:
                    return user_options(username)
                else:
                    return "Wrong pasword. Try agin."
        except Exception:
            print("Failure! Try agin.")

login()
