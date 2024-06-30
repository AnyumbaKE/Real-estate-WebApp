import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Categories, Post

class CategoriesType(DjangoObjectType):
    class Meta:
        model = Categories

class
class
class
class
class
class
class
class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PostInput(required=True)
    
    ok = graphene.Boolean()
    post = graphene.Field(PostType)
    
class Mutation(graphene.ObjectType):
    create_category = CreateCategories.Field()
    update_category = UpdateCategories.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
