from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home_view(request):

    # return render(request, template_name="calculator/index.html", context=f'Это страница простого помощника для приготовления блюд. ')
    return HttpResponse(f'Это страница простого помощника для приготовления блюд. '
                        f'Для получения списка ингридиентов наберите в строке запроса название блюда, '
                        f'например:http://127.0.0.1:8000/omlet/')

def recipe_view(request, recipe):
    servings = request.GET.get("servings", "")
    print(servings)
    if DATA.get(recipe)!=None:
        if servings:
            if int(servings) > 0:
                servings_recipe = {}
                for key, value in DATA[recipe].items():
                    servings_recipe[key] = value * int(servings)
                context = {
                    "recipe": servings_recipe

                }
        else:
            context = {
                "recipe": DATA[recipe]

            }

        return render(request, template_name="calculator/index.html", context=context)
    else:
        return HttpResponse(f'Такого рецепта я не знаю. Попробуйте ввести другой рецепт')

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
