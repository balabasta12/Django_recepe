from django.shortcuts import render
from django.http import HttpResponse

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

# Функции для отображения блюда и кол-во инг.
def omlet(request):  # Подсчёт инг. на кол-во человек
    req = request.GET.get('servings')
    omlet = {}

    if req:
        for i, v in DATA['omlet'].items():
            omlet[i] = v * int(req)
    else:
        for i, v in DATA['omlet'].items():
            omlet[i] = v

    return HttpResponse(f'Омлет: {omlet}')

def pasta(request):
    pasta = {}
    for i, v in DATA['pasta'].items():
        pasta[i] = v

    return HttpResponse(f'Паста: {pasta}')

def buter(request):
    buter = {}
    for i, v in DATA['buter'].items():
        buter[i] = v

    return HttpResponse(f'Бутер: {buter}')

# Функция для подсчёта кол-во инг. на 'n' персон
def calculator(request):
    name_recepe = request.GET.get('name')
    req = request.GET.get('servings')

    omlet = {}
    if name_recepe == 'omlet':
        for i, v in DATA['omlet'].items():
            omlet[i] = v * int(req)

    pasta = {}
    if name_recepe == 'pasta':
        for i, v in DATA['pasta'].items():
            pasta[i] = v * int(req)

    buter = {}
    if name_recepe == 'buter':
        for i, v in DATA['buter'].items():
            buter[i] = v * int(req)

    context = {"omlet": omlet,
               "pasta": pasta,
               "buter": buter}

    return render(request, 'calculator/index.html', context)

