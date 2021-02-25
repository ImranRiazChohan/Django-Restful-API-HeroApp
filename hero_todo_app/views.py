from django.shortcuts import render
from .models import Hero
from .serializer import HeroSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def Hero_list(request):
    hero=Hero.objects.all()
    list_serializer=HeroSerializer(hero,many=True)
    return Response(list_serializer.data)

@api_view(["POST"])
def Hero_Create(request):
    hero_create=HeroSerializer(data=request.data)
    if hero_create.is_valid():
        hero_create.save()
    return Response("Successfully Created")

@api_view(["DELETE"])
def Hero_Delete(request,pk):
    hero=Hero.objects.get(id=pk)
    hero.delete()
    return Response("Hero has been Deleted!")

@api_view(["PUT"])
def Hero_Update(request,pk):
    hero=Hero.objects.get(id=pk)
    hero_serializer=HeroSerializer(instance=hero,id=pk)
    if hero_serializer.is_valid():
        hero_serializer.save()
    return (hero_serializer.data)

@api_view(["GET"])
def Home(request):
    return Response("WELCOME TO RESTFRAME WORK \nWorks On HERO API")

@api_view(["GET"])
def Search_Hero(request,pk):
    hero=Hero.objects.get(id=pk)
    hero_serializer=HeroSerializer(hero,many=False)
    return Response(hero_serializer.data)