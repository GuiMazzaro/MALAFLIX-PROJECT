from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect 

from rest_framework.permissions import IsAuthenticated

#-----------------------------------------------------------------------CATEGORY API

class CategoriaAPI(APIView):

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):

        if pk == '':

            categoryData = Category.objects.all()            
            serializer = CategoryTable(categoryData, many=True)
            return Response(serializer.data)

        else:

            categoryData = Category.objects.get(id=pk)
            serializer = CategoryTable(categoryData)
            return Response(serializer.data)


    def post(self, request):   

        serializer = CategoryTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):

        categoryData = Category.objects.get(id=pk)
        serializer = CategoryTable(categoryData, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk=''):

        categoryData = Category.objects.get(id=pk)
        categoryData.delete()

        return Response({"msg": "Apagado com sucesso"})


#-----------------------------------------------------------------------MOVIES API

class MoviesAPI(APIView):

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):

        if pk == '':

            moviesData = Movies.objects.all()            
            serializer = MoviesTable(moviesData, many=True)
            return Response(serializer.data)

        else:

            moviesData = Movies.objects.get(id=pk)
            serializer = MoviesTable(moviesData)
            return Response(serializer.data)


    def post(self, request):   

        serializer = MoviesTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):

        moviesData = Movies.objects.get(id=pk)
        serializer = MoviesTable(moviesData, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk=''):

        moviesData = Movies.objects.get(id=pk)
        moviesData.delete()

        return Response({"msg": "Apagado com sucesso"})


#-----------------------------------------------------------------------SIGNATURE API

class SignatureAPI(APIView):

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):

        if pk == '':

            signatureData = Signature.objects.all()
            serializer = SignatureTable(signatureData, many=True)
            return Response(serializer.data)

        else:

            signatureData = Signature.objects.get(id=pk)
            serializer = SignatureTable(signatureData)
            return Response(serializer.data)


    def post(self, request):

        serializer = SignatureTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):

        signatureData = Signature.objects.get(id=pk)
        serializer = SignatureTable(signatureData, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk=''):

        signatureData = Signature.objects.get(id=pk)
        signatureData.delete()

        return Response({"msg": "Apagado com sucesso"})


#-----------------------------------------------------------------------USER API

class UsersAPI(APIView):

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):

        if pk == '':

            userData = Users.objects.all()
            serializer = UsersTable(userData, many=True)
            return Response(serializer.data)

        else:

            userData = Users.objects.get(id=pk)
            serializer = UsersTable(userData)
            return Response(serializer.data)


    def post(self, request):

        serializer = UsersTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):

        usersData = Users.objects.get(id=pk)
        serializer = UsersTable(usersData, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk=''):

        usersData = Users.objects.get(id=pk)
        usersData.delete()

        return Response({"msg": "Apagado com sucesso"})


#-----------------------------------------------------------------------FAVORITE API

class FavoriteAPI(APIView):

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):

        if pk == '':

            favoriteData = Favorite.objects.all()
            serializer = FavoriteTable(favoriteData, many=True)
            return Response(serializer.data)

        else:

            favoriteData = Favorite.objects.get(id=pk)
            serializer = FavoriteTable(favoriteData)
            return Response(serializer.data)


    def post(self, request):

        serializer = FavoriteTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):

        favoriteData = Favorite.objects.get(id=pk)
        serializer = FavoriteTable(favoriteData, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk=''):

        favoriteData = Users.objects.get(id=pk)
        favoriteData.delete()

        return Response({"msg": "Apagado com sucesso"})