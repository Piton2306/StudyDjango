from django.shortcuts import render


# Create your views here.
def index(request):
    data = {'title': 'Главная страница.',
            'values': ['Some', 'Hello', '123'],
            'obj': {'car': 'opel',
                    'age': 29,
                    'hobby': 'Apex', }}
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
