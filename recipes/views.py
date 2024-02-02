from django.shortcuts import get_list_or_404, render
from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id,
    #     is_published=True
    # ).order_by('-id')

    # if not recipes:
    #     return render(request, 'recipes/erros/404.html')
    
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id,
                              is_published=True).order_by('-id'))
    
    # return render(request, 'recipes/pages/category.html', context={
    #     'recipes': recipes,
    #     'title': f'{recipes.first().category.name} - Category | '
    # })

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def search(request):
    return render(request,'recipes/pages/search.html', context={
      'recipes': Recipe.objects.filter(is_published=True),
    })


def recipe(request, id):
    recipe = Recipe.objects.filter(pk=id, is_published=True).order_by('-id').first()

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe, #make_recipe(),
        'is_detail_page': True,
    })
