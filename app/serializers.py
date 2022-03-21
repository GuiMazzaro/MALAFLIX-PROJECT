from rest_framework import serializers
from .models import *

class CategoryTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Category
        fields = '__all__' 

class MoviesTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Movies
        fields = '__all__'

class SignatureTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Signature
        fields = '__all__'


class UsersTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Users
        fields = '__all__'

class FavoriteTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Favorite
        fields = '__all__'