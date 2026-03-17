#global values
users=[]
habits=[]
goals=[]
progress_list=[]
posts=[]
comments=[]
likes=[]
friendships=[]
communities=[]
memberships=[]
badges=[]
user_badges=[]

#id generations
def get_id(lst):
    return len(lst)+1

#class

class User:
    def __init__(self,username,email,password):
        self.user_id=get_id(users)
        self.username=username
        self.email=email
        self.password=password

    def createHabit(self):
        name=input("Enter habit name: ")
        freq=input("Enter frequency: ")
        h=Habit(self.user_id,name,freq)
        habits.append(h)
        print("Habit created")

    def viewHabits(self):
        for h in habits:
            if h.user_id==self.user_id:
                print(h.habit_id,h.habit_name,h.frequency)

    def postUpdate(self):
        content=input("Enter post: ")
        p=Post(self.user_id,content)
        posts.append(p)
        print("Posted")

    def addFriend(self):
        fid=int(input("Enter friend user id: "))
        friendships.append(Friendship(self.user_id,fid))
        print("Request sent")

class Habit:
    def __init__(self,user_id,name,freq):
        self.habit_id=get_id(habits)
        self.user_id=user_id
        self.habit_name=name
        self.frequency=freq

    def setGoal(self):
        val=float(input("Target value: "))
        unit=input("Unit: ")
        period=input("Period: ")
        g=Goal(self.habit_id,val,unit,period)
        goals.append(g)
        print("Goal set")

    def trackProgress(self):
        val=float(input("Done value: "))
        p=HabitProgress(self.habit_id,val)
        progress_list.append(p)
        print("Progress updated")

class Goal:
    def __init__(self,habit_id,val,unit,period):
        self.goal_id=get_id(goals)
        self.habit_id=habit_id
        self.target_value=val
        self.target_unit=unit
        self.target_period=period

class HabitProgress:
    def __init__(self,habit_id,val):
        self.habit_id=habit_id
        self.value_done=val
        self.completed=False

class Post:
    def __init__(self,user_id,content):
        self.post_id=get_id(posts)
        self.user_id=user_id
        self.content=content

class Comment:
    def __init__(self,post_id,user_id,text):
        self.comment_id=get_id(comments)
        self.post_id=post_id
        self.user_id=user_id
        self.text=text

class Like:
    def __init__(self,user_id,post_id):
        self.user_id=user_id
        self.post_id=post_id

class Friendship:
    def __init__(self,u1,u2):
        self.user_id=u1
        self.friend_id=u2

class Community:
    def __init__(self,name):
        self.community_id=get_id(communities)
        self.name=name


def find_user(uid):
    for u in users:
        if u.user_id==uid:
            return u
    return None

def find_habit(hid):
    for h in habits:
        if h.habit_id==hid:
            return h
    return None


def main():
    while True:
        print("\n1.Register\n2.Login\n3.Exit")
        ch=input("Choice: ")

        if ch=="1":
            username=input("Username: ")
            email=input("Email: ")
            password=input("Password: ")
            u=User(username,email,password)
            users.append(u)
            print("User created. ID:",u.user_id)

        elif ch=="2":
            uid=int(input("Enter user id: "))
            user=find_user(uid)

            if not user:
                print("User not found!")
                continue

            user_menu(user)

        elif ch=="3":
            break



def user_menu(user):
    while True:
        print("\n1.Create Habit\n2.View Habits\n3.Set Goal\n4.Track Progress\n5.Post\n6.Add Friend\n7.Logout")
        ch=input("Choice: ")

        if ch=="1":
            user.createHabit()

        elif ch=="2":
            user.viewHabits()

        elif ch=="3":
            hid=int(input("Habit ID: "))
            h=find_habit(hid)
            if h and h.user_id==user.user_id:
                h.setGoal()
            else:
                print("Invalid habit")

        elif ch=="4":
            hid=int(input("Habit ID: "))
            h=find_habit(hid)
            if h and h.user_id==user.user_id:
                h.trackProgress()
            else:
                print("Invalid habit")

        elif ch=="5":
            user.postUpdate()

        elif ch=="6":
            user.addFriend()

        elif ch=="7":
            break


main()