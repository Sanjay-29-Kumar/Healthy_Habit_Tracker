users={}
mail_index={}
next_userid=1

logged_userid=None

class User:
    def __init__(self,userid,username,passwordhash,mail):
        self.userid=userid
        self.username=username
        self.passwordhash=passwordhash
        self.mail=mail

    def __str__(self):
        return f"UserID:{self.userid}, Name:{self.username}, Email:{self.mail}"

    @staticmethod
    def register():
        global next_userid 

        username=input("Enter Username: ")
        password=input("Enter Password: ")
        mail=input("Enter Email: ")

        if mail in mail_index:
            print("User already exists")
            return
        
        userid=next_userid
        next_userid+=1

        user=User(userid,username,password,mail)
        users[userid]=user
        mail_index[mail]=userid
        print(f"User registered successfully. ID is {userid}")
        

    @staticmethod
    def login():
        global logged_userid

        mail=input("Enter Email: ")
        password=input("Enter Password: ")

        if mail not in mail_index:
            print("Mail not registered")
            return

        userid=mail_index[mail]
        user=users[userid]

        if user.passwordhash==password:
            logged_userid=userid
            print(f"Login successful. Welcome {user.username}")
        else:
            print("Invalid credentials")

    @staticmethod
    def view_users():
        if not users:
            print("No users registered")
            return
        
        for u in users.values():
            print(u)
    
    @staticmethod
    def logout():
        global logged_userid
        print("Logged out")
        logged_userid=None


while True:
    if logged_userid is None:
        print("\nWelcome...\n1.Register\n2.Login\n3.View Users\n4.Exit")
        ch=input("Enter choice: ")

        if ch=="1":
            User.register()
        elif ch=="2":
            User.login()
        elif ch=="3":
            User.view_users()
        elif ch=="4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
    
    else:
        print("\n1.View Profile\n2.Logout")
        ch=input("Enter choice: ")

        if ch=='1':
            print(users[logged_userid])
        elif ch=='2':
            User.logout()
        else:
            print("Invalid choice")