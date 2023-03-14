from django.http import HttpResponse
from .serializer import *
from rest_framework import generics, viewsets


def simple_page(request):
    return HttpResponse("Главная страница")


class AccountAPIList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


def get_domain(email: str) -> str:
    """Возвращает домен имейла"""

    try:
        _, domain = email.split('@')
    except ValueError:
        domain = ''

    return domain
