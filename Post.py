# Factory design pattern

from abc import ABCMeta, abstractclassmethod

from matplotlib import pyplot as plt
from matplotlib import image
import matplotlib
import SocialNetwork
import User

class IPost(metaclass=ABCMeta):
    _notifications = []
    def like(post, other_user):
            print(f"notification to {post.username}: {other_user.username} liked your post")
            str = f"{other_user.username} liked your post\n"
            IPost._notifications.append(str)


    def comment(post, other_user, text):
            print(f"notification to {post.username}: {other_user.username} commented on your post: {text}")
            str = f"{other_user.username} commented on your post\n"
            IPost._notifications.append(str)
            

        



class Text(IPost):
    def __init__(self, name, type, actual_text):
        self.username = name
        self.type = type
        self.actual_text = actual_text
        self.num_of_likes = 0
        print(f"{self.username} published a post:\n")
        print(f"{actual_text}\n")
        

    
    def __str__(self):
        return f"{self.username} published a post:\n {self.actual_text}"
        
    
    def like(self, other_user):
        IPost.like(self, other_user)
        self.num_of_likes +=1
    
    def comment(self, other_user, text):
        IPost.comment(self, other_user, text)



        
    

class Image(IPost):
    def __init__(self, name, description):
        self.username = name
        self.description = description
        print(f"{self.username} posted a picture\n")
        self.num_of_likes = 0
    
    def __str__(self):
        return f"{self.username} posted a picture \n"
    
    def display(self):
        #imagine picture here
        print("Shows picture")
    
    def like(self, other_user):
        IPost.like(self, other_user)
        self.num_of_likes +=1
    
    def comment(self, other_user, text):
        IPost.comment(self, other_user, text)
    

    





class Sale(IPost):
    def __init__(self, name, type, car_info, cost, location):
        self.username = name
        self.type = type
        self.car_info = car_info
        self.cost = cost
        self.location = location
        print(f"{self.username} posted a product for sale: \n")
        print(f"For sale! {self.car_info}, price: {self.cost}, pickup from: {self.location}\n")
        self.num_of_likes = 0
        
    
    def __str__(self):
        return f"{self.username}'s product is sold\n{self.username} posted a product for sale: \n Sold! {self.car_info}, price: {self.cost}, pickup from {self.location}\n"



    def discount(self, discount_price, password):
        if(SocialNetwork.SocialNetwork.correct_password(self.username, password)):
            self.cost = (100.0 - discount_price)* self.cost/100.0
            print(f"Discount on {self.username} product! the new price is: {self.cost}")
    

    def sold(self, password):
        if(SocialNetwork.SocialNetwork.correct_password(self.username, password)):
            print(f"{self.username}'s product is sold\n")
            print(f"{self.username} posted a product for sale:\n")
            print(f"Sold! {self.car_info}, price: {self.cost}, pickup from: {self.location}")

    
    def like(self, other_user):
        IPost.like(self, other_user)
        self.num_of_likes +=1
    
    def comment(self, other_user, text):
        IPost.comment(self, other_user, text)




class PostFactory:
    @staticmethod
    def build_post(user_username, *args):
        if (args[0] == "Text"):
            new_post = Text(user_username, args[0], args[1])
            return new_post
        if (args[0] == "Image"):
            new_post = Image(user_username, args[0])
            return new_post
        if (args[0]== "Sale"):
            new_post = Sale(user_username, args[0], args[1], args[2], args[3])
            return new_post
        