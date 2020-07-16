from django.urls import path
from stories.views import HomePage , about ,StoryListView , RecipeListView , StoryDetailView , RecipeDetailView , ContactView, \
    CreateStoryView , StoryUpdateView , StoryDeleteView , CreateRecipeView , RecipeUpdateView , RecipeDeleteView , SaveRecipeView, \
    SavedRecipeListView



urlpatterns = [
    path('', HomePage.as_view(), name = 'home'),
    path('about/', about , name = 'about'),
    path('recipes/', RecipeListView.as_view() , name = 'recipes'),
    path('recipes/<str:slug>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('stories/', StoryListView.as_view() , name = 'stories'),
    path('stories/<str:slug>/', StoryDetailView.as_view(), name='story_detail'),
    path('contact/', ContactView.as_view() , name = 'contact'),
    path('create-story',CreateStoryView.as_view(), name = 'create_story'),
    path('create-recipe',CreateRecipeView.as_view(), name = 'create_recipe'),
    path('update-story/<str:slug>/', StoryUpdateView.as_view(), name = 'update_story') ,
    path('delete-story/<str:slug>/', StoryDeleteView.as_view(), name = 'delete_story') ,
    path('update-recipe/<str:slug>/', RecipeUpdateView.as_view(), name = 'update_recipe') ,
    path('delete-recipe/<str:slug>/', RecipeDeleteView.as_view(), name = 'delete_recipe') ,
    path('save-recipe/<int:pk>/', SaveRecipeView.as_view(), name = 'save_recipe') ,
    path('saved-recipes/', SavedRecipeListView.as_view(), name='saved_recipes'),
]