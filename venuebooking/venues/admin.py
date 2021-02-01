from django.contrib import admin
from venues.models import Venues
from venues.models import Shows
from venues.models import Artist
from venues.models import Genre

# Register your models here.
admin.site.register(Venues)
admin.site.register(Shows)
admin.site.register(Artist)
admin.site.register(Genre)
