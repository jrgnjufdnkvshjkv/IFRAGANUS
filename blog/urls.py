from django.urls import path
from .views import index, kurslar, konsultatsiya

urlpatterns = [
    path('index/', index, name='index'),
    path('kurslar/', kurslar, name='kurslar',),
    path('konsultatsiya/', konsultatsiya, name='konsultatsiya'),

]
