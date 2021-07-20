from django.test import TestCase

# Create your tests here.
from django.http import HttpResponse


# Create your views here.

obj= {'car': 'opel',
        'age': 29,
        'hobby': 'Apex', }
for i in obj:
    if i == 'hobby':
        print(i)