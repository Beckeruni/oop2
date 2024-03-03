import SocialNetwork
import User

# Factory Pattern
class PostFactory:
    @staticmethod
    def posting(post_type, *args, **kwargs):
        if post_type == "text":
            return TextPost(*args, **kwargs)
        elif post_type == "image":
            return ImagePost(*args, **kwargs)
        elif post_type == "sale":
            return SalePost(*args, **kwargs)
        else:
            raise ValueError("Invalid post type")


class Post:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.likes = set()
        self.comments = []

    def like(self, other_user: User):
        if other_user in SocialNetwork.SocialNetwork.SocialNetwork.users:
           if(other_user is not self.user):
             user.update("{} liked your post".format(self.content))

    def comment(self, other_user: User, text):
        comment = "{}: {}".format(other_user.username, text)
        self.comments.append(comment)
        user.update("Commented on your post: {}".format(self.content))


class TextPost(Post):
    pass


class ImagePost(Post):
    def __init__(self, content, user, image_path):
        super().__init__(content, user)
        self.image_path = image_path

    def display(self):
        img = mpimg.imread(self.image_path)
        imgplot = plt.imshow(img)
        plt.show()


class SalePost(Post):
    def __init__(self, content, user, description, price, location):
        super().__init__(content, user)
        self.description = description
        self.price = price
        self.location = location
        self.sold = False

    def discount(self, percentage, password: str):
        if self.sold is False:
           if password == self.user.password:
              self.price *= (100 - percentage) / 100
              print("Discount on {} product! the new price is: {}".format(self.user, self.price))
           else:
              print("this is not your post!!")
            
    def sold(self, password: str):
        if password is self.user.password: 
          self.sold = True
        
    def print_sold(self):
        print("this item sold by {}".format(self.user))

    def display(self):
        if self.sold is True:
            isSold= "Sold!"
        else:
            isSold= "For sale!"
            
        print("{} {}, price: {}, pickup from: {}".format(isSold, self.content, self.price, self.location))
