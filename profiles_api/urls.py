from django.urls import path
from profiles_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),   #std. func we call to convert our apiview class in views.py into urls
]