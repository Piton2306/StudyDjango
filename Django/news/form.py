from .models import article
from django.forms import ModelForm


class articleForm(ModelForm):
    class Meta:
        model = article
        fields = ['title', 'anons', 'ful_text', 'data']
