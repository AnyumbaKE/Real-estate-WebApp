import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Categories, Post

class CategoriesType(DjangoObjectType):
    class Meta:
        model = Categories