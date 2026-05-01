from django.urls import path
from .views import home, upload_resume

urlpatterns = [
    path('', home),                 #  homepage
    path('upload/', upload_resume) #  API
]