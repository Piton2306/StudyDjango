from django.shortcuts import render
from .models import article
from .form import articleForm


# Create your views here.
def news_home(request):
    news = article.objects.order_by("-data")
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    form = articleForm()
    data = {'form': form
            }
    return render(request, 'news/create.html',data)
