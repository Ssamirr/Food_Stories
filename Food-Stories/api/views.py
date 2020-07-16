from django.shortcuts import render, get_object_or_404
from stories.models import Recipe , Story, Category
from api.serializers import RecipeSerializer, RecipeReadSerializer , StoryReadSerializer, StorySerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT


@api_view(http_method_names=('GET', 'POST',))
def recipes_api(request):
    response_data = {
        'message': 'success',
        'action': 'read'
    }
    status_code = HTTP_200_OK
    if request.method == 'GET':
        category_titles = request.GET.get('categories')
        tag_titles = request.GET.get('tags')
        if category_titles:
            category_title = category_titles.split(",")
            recipes = Recipe.objects.filter(category__title__in = category_title)
        elif tag_titles:
            tag_title = tag_titles.split(",")
            recipes = Recipe.objects.filter(tags__title__in = tag_title)
        else :
            recipes = Recipe.objects.filter(is_published=True)
        serializer = RecipeReadSerializer(recipes, many=True)
        response_data['recipe'] = serializer.data
        # return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        recipe_data = request.data
        serializer = RecipeSerializer(data=recipe_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['recipe'] = serializer.data
        response_data['action'] = 'modify'
        status_code = HTTP_201_CREATED
        # return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(response_data, status=status_code)



@api_view(('GET', 'PUT', 'PATCH', 'DELETE'))
def recipe(request, id):
    response_data = {
        'message': 'success',
        'action': 'read'
    }
    status_code = HTTP_200_OK
    if request.method == 'GET':
        recipe = get_object_or_404(Recipe, id=id)
        serializer = RecipeReadSerializer(recipe)
        response_data['recipe'] = serializer.data
    elif request.method == 'PUT':
        recipe = get_object_or_404(Recipe, id=id)
        serializer = RecipeSerializer(recipe, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['recipe'] = serializer.data
        response_data['action'] = 'modify'
    elif request.method == 'PATCH':
        recipe = get_object_or_404(Recipe, id=id)
        serializer = RecipeSerializer(instance=recipe, data=request.data, partial=True, )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['recipe'] = serializer.data
        response_data['action'] = 'partial_modify'
    elif request.method == 'DELETE':
        recipe = get_object_or_404(Recipe, id=id)
        recipe.delete()
        response_data = {}
        status_code = HTTP_204_NO_CONTENT
    return Response(response_data, status=status_code)


@api_view(http_method_names=('GET', 'POST',))
def stories_api(request, *args, **kwargs):
    response_data = {
        'message': 'success',
        'action': 'read'
    }
    status_code = HTTP_200_OK
    if request.method == 'GET':
        category_titles = request.GET.get('categories')
        if category_titles:
            category_title = category_titles.split(",")
            stories = Story.objects.filter(category__title__in = category_title)
        elif tag_titles:
            tag_title = tag_titles.split(",")
            recipes = Story.objects.filter(tags__title__in = tag_title)
        else:
            stories = Story.objects.filter(is_published=True)

        serializer = StoryReadSerializer(stories, many=True)
        response_data['story'] = serializer.data
        # return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        story_data = request.data
        serializer = StorySerializer(data=story_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['story'] = serializer.data
        response_data['action'] = 'modify'
        status_code = HTTP_201_CREATED
        # return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(response_data, status=status_code)



@api_view(('GET', 'PUT', 'PATCH', 'DELETE'))
def story(request, id):
    response_data = {
        'message': 'success',
        'action': 'read'
    }
    status_code = HTTP_200_OK
    if request.method == 'GET':
        story = get_object_or_404(Story, id=id) 
        serializer = StoryReadSerializer(story)
        response_data['story'] = serializer.data
    elif request.method == 'PUT':
        story = get_object_or_404(Story, id=id)
        serializer = StorySerializer(story, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['story'] = serializer.data
        response_data['action'] = 'modify'
    elif request.method == 'PATCH':
        story = get_object_or_404(Story, id=id)
        serializer = StorySerializer(instance=story, data=request.data, partial=True, )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['story'] = serializer.data
        response_data['action'] = 'partial_modify'
    elif request.method == 'DELETE':
        story = get_object_or_404(Story, id=id)
        story.delete()
        response_data = {}
        status_code = HTTP_204_NO_CONTENT
    return Response(response_data, status=status_code)


@api_view(http_method_names=('GET', 'POST',))
def categories_api(request):
    response_data = {
        'message': 'success',
        'action': 'read'
    }
    status_code = HTTP_200_OK
    if request.method == 'GET':
        categories = Category.objects.filter(is_published=True)
        serializer = CategorySerializer(categories, many=True)
        response_data['category'] = serializer.data
        # return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        category_data = request.data
        serializer = CategorySerializer(data=category_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['category'] = serializer.data
        response_data['action'] = 'modify'
        status_code = HTTP_201_CREATED
        # return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(response_data, status=status_code)



@api_view(('GET', 'PUT', 'PATCH', 'DELETE'))
def category(request, id):
    response_data = {
        'message': 'success',
        'action': 'read'
    }
    status_code = HTTP_200_OK
    if request.method == 'GET':
        category = get_object_or_404(Category, id=id) 
        serializer = CategorySerializer(category)
        response_data['category'] = serializer.data
    elif request.method == 'PUT':
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['category'] = serializer.data
        response_data['action'] = 'modify'
    elif request.method == 'PATCH':
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(instance=category, data=request.data, partial=True, )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['category'] = serializer.data
        response_data['action'] = 'partial_modify'
    elif request.method == 'DELETE':
        category = get_object_or_404(Category, id=id)
        category.delete()
        response_data = {}
        status_code = HTTP_204_NO_CONTENT
    return Response(response_data, status=status_code)


# @api_view(http_method_names=('GET', 'POST',))
# def story_for_category(request, slug):
#     response_data = {
#         'message': 'success',
#         'action': 'read'
#     }
#     status_code = HTTP_200_OK
#     if request.method == 'GET':
#         story = get_object_or_404(Story, category_title=slug) 
#         serializer = StoryReadSerializer(story)
#         response_data['story'] = serializer.data
#     return Response(response_data, status=status_code)