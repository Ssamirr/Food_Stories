from django.shortcuts import render , redirect, get_object_or_404
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView ,TemplateView , View
from stories.models import Category, Recipe , Story , SavedArticle
from stories.forms import ContactForm , StoryForm, RecipeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.http import HttpResponseForbidden , HttpResponse
from django.core.exceptions import PermissionDenied
import random


# Create your views here.

# def home(request):
#     recipes = Recipe.objects.all()[:2]
#     stories = Story.objects.all()[:4]
#     context = {
#         'recipes' : recipes,
#         'stories' : stories
#     }
#     return render(request,'index.html',context)

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        if Story.objects.count()>0:
            print('aaaaaaa')
            random_story = random.choice(Story.objects.all())
            context['random_story'] = random_story
        context['recipes'] = Recipe.objects.all().order_by('-show_home_page')[:2]
        context['stories'] = Story.objects.all().order_by('-show_home_page')[:4]
        return context


def about(request):
    return render(request,'about.html')

class StoryListView(ListView):
    model = Story
    template_name = 'stories.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)

class StoryDetailView(DetailView):
    model = Story
    template_name = 'single.html'

# def recipes(request):
#     recipes = Recipe.objects.filter(is_published=True)
#     context = {
#         'recipes': recipes
#     }
#     return render(request, 'recipes.html', context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'single.html'

# def stories(request):
#     stories = Story.objects.filter(is_published=True)
#     context = {
#         'stories': stories
#     }
#     return render(request, 'strories.html', context)


# def recipe_detail(request, slug):
#     print(slug)
#     # recipe = Recipe.objects.get(slug=slug)
#     recipe = get_object_or_404(Recipe, slug=slug)
#     context = {
#         'object': recipe
#     }
#     return render(request, 'single.html', context)


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Mesajiniz gonderildi!!')
        return super().form_valid(form)

class CreateStoryView(LoginRequiredMixin,CreateView):
    form_class = StoryForm
    template_name = 'create_story.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_author:
            raise PermissionDenied
            # return HttpResponseForbidden('403 Forbidden')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        story = form.save(commit=False)
        story.author = self.request.user
        story.save()
        return super().form_valid(form)

class CreateRecipeView(LoginRequiredMixin,CreateView):
    form_class = RecipeForm
    template_name = 'create_recipe.html'
    # permission_required = ('stories.add_recipe')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_author:
            raise PermissionDenied
            # return HttpResponseForbidden('403 Forbidden')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = self.request.user
        recipe.save()
        return super().form_valid(form)

class StoryUpdateView(LoginRequiredMixin,UpdateView):
    form_class = StoryForm
    model = Story
    template_name = 'create_story.html'

class StoryDeleteView(LoginRequiredMixin,DeleteView):
    model = Story
    success_url = reverse_lazy('stories')
    http_method_names = ('get',)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class RecipeUpdateView(LoginRequiredMixin,UpdateView):
    form_class = RecipeForm
    model = Recipe
    template_name = 'create_recipe.html'

class RecipeDeleteView(LoginRequiredMixin,DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes')
    http_method_names = ('get',)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class SaveRecipeView(View):
    def get(self, *args, **kwargs):
        recipe_id = kwargs.get('pk')
        message = 'Melumat elave edildi'
        recipe = get_object_or_404(Recipe, id=recipe_id)
        
        if self.request.user.is_authenticated:
            save_article, created = SavedArticle.objects.get_or_create(user=self.request.user, recipe=recipe)
            if not created:
                message = 'Melumat evvel elave edilmisdi'
            response = HttpResponse(message)
        else:
            saved_articles = self.request.COOKIES.get('saved_articles', '')
            print('saved_articles', saved_articles)
            if str(recipe_id) not in saved_articles.split(';'):
                saved_articles += str(recipe_id) + ";"
            response = HttpResponse(message)
            response.set_cookie('saved_articles', saved_articles)
        # messages.success(self.request, message)
        return response

class SavedRecipeListView(ListView):
    model = Recipe
    template_name = 'saved_recipes.html'
    paginate_by = 2

    def get_queryset(self, ):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            user_saved_articles_ids = self.request.user.saved_articles.values_list('id', flat=True)
            return queryset.filter(id__in=user_saved_articles_ids)
        else:
            saved_recipes = self.request.COOKIES.get('saved_articles')
            if saved_recipes:
                saved_recipe_ids = [int(id) for id in saved_recipes.split(';') if id and id != 0]
                queryset = super().get_queryset()
                return queryset.filter(id__in=saved_recipe_ids)
            return None
    



# form yaratmadan bele elemek olar , html faylinda {{form}} yazmaqla
# class CreateStoryView(CreateView): 
#     model = Story
#     fields = '__all__'
#     template_name = 'create_story.html'


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Mesajiniz gonderildi!!')
#             return redirect('/')
#         else:
#             messages.error(request, 'Mesajiniz gonderilmedi')
#     else:
#         form = ContactForm()
#     context = {
#         'form' : form
#     }
#     return render(request, 'contact.html', context)










