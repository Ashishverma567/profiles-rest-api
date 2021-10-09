from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-views')
                 #name of url    to access viewset in views.py
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),   #std. func we call to convert our apiview class in views.py into urls
    path('', include(router.urls))
]

