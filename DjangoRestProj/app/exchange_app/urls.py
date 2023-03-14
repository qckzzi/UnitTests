from django.urls import path, include
from .views import *

urlpatterns = [
    path('', simple_page),
    path('api/v1/accounts/', AccountAPIList.as_view()),
    path('api/v1/cars/', CarAPIList.as_view())
]
