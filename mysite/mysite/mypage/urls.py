from django.urls import path
from .views import index, items


urlpatterns = [
    path('', index, name="index"),
    path('item/', items, name="item"),
]