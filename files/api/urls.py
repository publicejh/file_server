from django.urls import path
from .views import ImageInfoCreateView


urlpatterns = [
    path('images', ImageInfoCreateView.as_view()),
]
