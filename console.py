users={}
mail_index={}
next_userid=1

habit_index={}
next_habitid=1

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


class Habit:
    def __init__(self,habitid,userid,habitname,frequency):
        self.habitid=habitid
        self.userid=userid
        self.habitname=habitname
        self.frequency=frequency

    def __str__(self):
        return f"Habit ID: {self.habitid}, Habit Name: {self.habitname}, Frequency: {self.frequency}"

    @staticmethod
    def addHabit():
        global next_habitid

        habitname=input("Enter Habit Name: ")
        frequency=input("Enter Frequency: ")

        habit=Habit(next_habitid,logged_userid,habitname,frequency)
        habit_index[next_habitid]=habit

        print("Habit added")
        next_habitid+=1

    @staticmethod
    def viewHabit():
        found=False
        for h in habit_index.values():
            if h.userid==logged_userid:
                print(h)
                found=True

        if not found:
            print("No habits found")
    
    @staticmethod
    def deleteHabit():
        hid=int(input("Enter Habit ID: "))

        if hid in habit_index and habit_index[hid].userid==logged_userid:
            del habit_index[hid]
            print("Habit deleted")
        else:
            print("Invalid Habit ID")


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
        print("\n1.Add Habit\n2.View Habits\n3.Delete Habit\n4.View Profile\n5.Logout")
        ch=input("Enter choice: ")

        if ch=="1":
            Habit.addHabit()
        elif ch=="2":
            Habit.viewHabit()
        elif ch=="3":
            Habit.deleteHabit()
        elif ch=="4":
            print(users[logged_userid])
        elif ch=="5":
            User.logout()
        else:
            print("Invalid choice")