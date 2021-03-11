from django.urls import path

from . import views

urlpatterns = [
    path(r'api/v1/event/', views.aggregate, name='event-url'),
    path(r'api/v1/analyze/', views.analyze, name='analyze-url'),
]
