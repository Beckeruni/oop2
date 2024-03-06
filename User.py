import matplotlib
from matplotlib import pyplot as plt
import Post, User
class Observer:
    def update(creator_name, post):
        pass

class ConcreteObserver(Observer):

    def update(self, post):
        if(type(post) == Post.Text):
            print(f"{post.username} published a post: \n")
            print(f"{post}\n")
        
        if(type(post) == Post.Image):
            print(f"{post.username} posted a picture")
        
        if(type(post) == Post.Sale):
            print(f"{post.username} posted a product for sale: \n")
            print(f"For sale! {post.car_info}, price: {post.cost}, pickup from: {post.location} \n")
            
        



class Subject(Observer):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.following = set()
        self.number_of_posts = 0
        self._postnotifications = []
        self._observers = []
        self.list_of_posts = []

    def __str__(self):
        return f"User name: {self.username}, Number of posts:{self.number_of_posts}, Number of followers: {len(self._observers)}"
    
    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer):
        self._observers.remove(observer)
    

    def notify_observers(self, post):
        for observer in self._observers:
            if(type(observer) == User.Subject):
                observer.update(post)
                str_info = " has a new post\n"
                observer._postnotifications.append(self.username + str_info)


    def follow(self, other_user):
        if(type(other_user) == User.Subject):
            other_user._observers.append(self)
            print(f"{self.username} started following {other_user.username} \n")


    def unfollow(self, other_user):
        if(type(other_user) == User.Subject):
            other_user._observers.remove(self)
            print(f"{self.username} unfollowed {other_user.username}")



    def publish_post(self, *args):
        newPost = Post.PostFactory.build_post(self.username, *args)
        self.notify_observers(newPost)
        self.number_of_posts +=1
        self.list_of_posts.append(newPost)
        return newPost
    

    
    def print_notifications(self):
        print(f"{self.username}'s notifications:\n")
        for notification in self._postnotifications:
            print(notification)
        for post in self.list_of_posts:
            if(type(post) == (Post.Text) or type(post) == Post.Image or type(post) == Post.Sale):
                for notification in post._notifications:
                    print(notification)
               
               



        





