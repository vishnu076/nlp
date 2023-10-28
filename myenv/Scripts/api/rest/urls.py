from django.urls import path
from .views import *
urlpatterns=[
    path('api/',mood.as_view(),name="mood")
]