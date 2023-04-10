from django.urls import path 
from api import views

urlpatterns = [
    path('candidates/',views.CanList.as_view()),
]
