from venues.models import Shows, Venues, Genre, Artist
from rest_framework import serializers

class ShowsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shows
        fields = ['show_name', 'venue', 'artist', 'time', 'date', 'charges']


class VenuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venues
        fields = ['venue_name', 'address','website', 'contact']


class ArtistsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist_name', 'music_type', 'intro']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']