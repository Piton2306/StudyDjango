from django.shortcuts import render, redirect
from .models import article
from .form import articleForm
from django.views.generic import DetailView


def news_home(request):
    news = article.objects.order_by("-date")
    return render(request, 'news/news_home.html', {'news': news})


class news_detail_view(DetailView):
    model = article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


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
