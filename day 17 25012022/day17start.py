class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.user_name = user_name
        self.following = 0
        self.follower = 0

    def enter_follower(self,user):
        user.follower += 1
        self.following +=1


user_1 = User("001","Hoang")
user_2 = User("001","Khoa")

user_1.enter_follower(user_2)

print(user_1.following)
print(user_1.follower)
print(user_2.following)
print(user_2.follower)