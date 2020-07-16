from django.urls import path
from api.views import recipes_api , recipe, stories_api, story, categories_api, category

urlpatterns = [
    path('recipes/', recipes_api , name = 'recipes'),
    path('recipes/<int:id>/', recipe, name='api_recipe'),
    path('stories/', stories_api , name = 'stories'),
    path('stories/<int:id>/', story, name='api_story'),
    # path('stories/?categories=<slug:str>/', story_for_category, name='story_for_category'),
    path('categories/', categories_api , name = 'categories'),
    path('categories/<int:id>/', category, name='api_categories'),
]
