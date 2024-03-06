import string
from abc import ABCMeta, abstractstaticmethod
import SocialNetwork
import User
import Post

tuple_of_user_and_password = []
#singlton design pattern
class ISocialNetwork(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_name():
        """implement in child class"""




class SocialNetwork(ISocialNetwork):
    __instance = None
    users_logged_in = set()
    all_users = set()

    @staticmethod
    def get_name():
        if SocialNetwork.__instance == None:
            return None
        return SocialNetwork.__instance.name

    def __init__(self, name):
        if(SocialNetwork.__instance != None):
            raise Exception("Already have a network")
        self.name = name
        SocialNetwork.__instance = self
        print(f"The social network {name} was created!")

    def __str__(self):
        ans = self.name + " social network\n"
        for user in self.all_users:
            if(type(user) == User.Subject):
                ans += user.__str__()
                ans += "\n"
        return ans





    def sign_up(self, username, password):
        if(len(password)>9 or len(password)<3):
                raise Exception("This Password is not secure, try another ")
        for pair in tuple_of_user_and_password:
            if(pair[1] == password):
                raise Exception("Sorry, password is taken already")
        new_user = User.Subject(username, password)
        tuple_of_user_and_password.append((username, password))
        self.users_logged_in.add(username)
        self.all_users.add(new_user)
        return new_user
    


    def log_in(self, username, password):
        if(SocialNetwork.correct_password(username, password)):
            print(f"{username} connected")
            self.users_logged_in.add(username)
        
    def log_out(self, username):
        print(f"{username} disconnected")
        self.users_logged_in.remove(username)


    def correct_password(username1, password1):
        for info in tuple_of_user_and_password:
            if info[0] == username1 and info[1] == password1:
                return True
        return False

    



   
    
