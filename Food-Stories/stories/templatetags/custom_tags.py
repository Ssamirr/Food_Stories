from django.template import Library
from stories.models import Category , Story , Recipe , USER_MODEL

register = Library()

@register.simple_tag
def category():
    categories = Category.objects.all().order_by('-show_page')[:3]
    context =categories
    return context

@register.simple_tag
def informations():
    stories = Story.objects.count()
    recipes = Recipe.objects.count()
    users = USER_MODEL.objects.count()
    context = {
        'stories' : stories,
        'recipes' : recipes,
        'users' : users,
        'daily_visitors' : '100'
    }
    return context



