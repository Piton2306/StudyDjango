from django.shortcuts import render,redirect
from .models import article
from .form import articleForm


# Create your views here.
def news_home(request):
    news = article.objects.order_by("-date")
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = articleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'Форма была не верной'

    form = articleForm()
    data = {
        'form': form,
        'error': error, }

    return render(request, 'news/create.html', data)
