from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UsersViewSet)

urlpatterns = [
    path('hello/', views.hello_world),
] + router.urls 