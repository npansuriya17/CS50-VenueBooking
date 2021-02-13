from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils.timezone import now

class User(AbstractUser):
    pass


class Posts(models.Model):
    posted_by_user = models.ForeignKey('User',on_delete=models.CASCADE,related_name='user_posted')
    content = models.CharField(max_length=2000, blank=False, null=False)
    posted_time = models.DateTimeField(default=now)

    def __str__(self):
        return '%s %s %s' % (str(self.posted_by_user), self.content, self.posted_time)

    def serialize(self):
        return {
            "id": self.id,
            "posted_by_user": self.posted_by_user.username,
            "content": self.content,
            "posted_time": self.posted_time.strftime("%b %d %Y, %H:%M %p"),
        }

class Follow(models.Model):
    following = models.ForeignKey('User', on_delete=models.CASCADE, related_name='following_user')
    follower = models.ForeignKey('User', on_delete=models.CASCADE ,related_name='follower_user')

    def __str__(self):
        return '%s %s' % (str(self.following),str(self.follower))
    
    def serialize(self):
        return {
            "id": self.id,
            "following": self.following.username,
            "follower": self.follower.username,
        }
    

class Likes(models.Model):
    post = models.ForeignKey('Posts',on_delete=models.CASCADE)
    liked_by_user = models.ForeignKey('User',on_delete=models.CASCADE,related_name='user_liked')

    def __str__(self):
        return '%s %s' % (str(self.post), str(self.liked_by_user))
    
    def serialize(self):
        return {
            "id": self.id,
            "post": self.post,
            "liked_by_user": self.liked_by_user.username,
        }
