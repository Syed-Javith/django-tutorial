from django.urls import path
from . import views
urlpatterns = [
    path('hello/',view=views.hello_template),
    path('<str:name>/',views.home),
]
