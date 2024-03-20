from django.urls import path

from .views import index,index2


urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', index2, name='index2')

]

