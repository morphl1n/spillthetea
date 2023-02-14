from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profilePicture = models.ImageField(upload_to='profile_pics/', blank=True, default='default-profile-pic.png')
    pass


class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    content = models.TextField(null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
   
    

    def __str__(self):
        return f"Creator: {self.creator} Timestamp:{self.timestamp} Content: {self.content}"
        

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followReceiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followReceiver")

    def __str__(self):
        return f"{self.follower} follows {self.followReceiver}"

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likedPost")
    likedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likedBy")

    def __str__(self):
        return f"{self.likedBy} liked {self.post}"