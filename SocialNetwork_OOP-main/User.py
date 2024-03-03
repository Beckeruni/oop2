from SocialNetwork.Post import TextPost
from SocialNetwork.Post import PostFactory
from SocialNetwork.SocialNetwork import SocialNetwork
import Post
from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, action: str):
        pass

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self, action: str):
        pass

class User(Observer):
    log = None

    # any new user has username, password
    # also has data - followers and posts
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = set()
        self.posts = []
        self.log = None
        self.notifications = []


    def __new__(cls, *args, **kwargs):
        # Check if the user with the same username already exists
        existing_user = next((user for user in cls.users if user.username == kwargs.get('username')), None)
        if existing_user:
            return existing_user
        else:
            return super().__new__(cls)

    # set the followers the user has
    def follow(self, other_user):
        if other_user != self:
            other_user.add_follower(self)
            return "{} started following {}".format(self.username, other_user)

    # add followers to user
    def add_follower(self, follower):
        self.followers.add(follower)

    def publish_post(self, _type: str ,content: str):
        post = TextPost(content, self)   # the base case- only text
        self.posts.append(post)    # add to post`s user, contain info, likes and comments
        Post.PostFactory.posting(post_type=_type)
        if _type is "Text":
          self.notify_followers("{} published a post: {}".format(self.username, content))

        if _type is "Image":
            self.notify_followers("{} posted a picture".format(self.username))

        if _type is "Sale":
            self.notify_followers(" {} posted a product for sale: {}".format(self.username, content))

    def notify_followers(self, message):
        for follower in self.followers:
            follower.update(message)


    def print_notifications(self, user):
        for noti in self.notifications:
            print("notification to {}: {}".format(self.username, self.notifications[noti]))

    def print(self, user):
        print("User name: {}, Number of posts: {}, Number of followers: {}".format(self.username, len(self.posts), len(self.followers)))
    def update(self, action):
        self.notifications.append ("Notification for {}: {}".format(self.username, action))

    
