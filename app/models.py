import re
from turtle import mode
from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Movies(models.Model):

    name = models.CharField(max_length=150)
    categoryFK = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Signature(models.Model):

    nameSignature = models.CharField(max_length=150)
    valueSignature = models.IntegerField()

    def __str__(self):
        return self.nameSignature

class Users(models.Model):

    nameUser = models.CharField(max_length=150)
    emailUser = models.CharField(max_length=150)
    foneUser = models.CharField(max_length=30)
    statusUser = models.BooleanField()
    signatureFK = models.ForeignKey(Signature, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameUser

class Favorite(models.Model):

    movieFK = models.ForeignKey(Movies, on_delete=models.CASCADE)
    userFK = models.ForeignKey(Users, on_delete=models.CASCADE)