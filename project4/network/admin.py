from django.contrib import admin
from network.models import User, Posts, Likes, Follow

# Register your models here.

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Likes)
admin.site.register(Follow)