from django.urls import path
from .views import ImageInfoCreateView, ChatImageUploadAndSendView


urlpatterns = [
    path('images', ImageInfoCreateView.as_view()),
    path('chat-images', ChatImageUploadAndSendView.as_view()),
]
