from django.contrib import admin
from .models import *

class auxCategory(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

class auxMovies(admin.ModelAdmin):
    list_display = ('id','name', 'categoryFK')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 10

class auxSignature(admin.ModelAdmin):
    list_display = ('id','nameSignature', 'valueSignature')
    list_display_links = ('nameSignature',)
    search_fields = ('nameSignature',)
    list_per_page = 10


class auxUsers(admin.ModelAdmin):
    list_display = ('id','nameUser', 'emailUser', 'foneUser', 'statusUser', 'signatureFK')
    list_display_links = ('nameUser',)
    search_fields = ('nameUser',)
    list_per_page = 10

class auxFavorite(admin.ModelAdmin):
    list_display = ('id','movieFK', 'userFK')
    list_display_links = ('movieFK',)
    search_fields = ('movieFK',)
    list_per_page = 10


admin.site.register(Category, auxCategory)
admin.site.register(Movies, auxMovies)
admin.site.register(Signature, auxSignature)
admin.site.register(Users, auxUsers)
admin.site.register(Favorite, auxFavorite)