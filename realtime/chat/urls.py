from django.urls import path, include

from .views import IndexView, SalaView


urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('chat/<str:nome_sala>/', SalaView.as_view(), name='sala')
]
