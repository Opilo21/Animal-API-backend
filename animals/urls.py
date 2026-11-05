from django.urls import path
from .views import(AnimalListCreateView, AnimalRetrieveUpdateDeleteView)


urlpatterns = [
    path('animals/', AnimalListCreateView.as_view(), name='all_Animal'),

    path('animals/<int:pk>/', AnimalRetrieveUpdateDeleteView.as_view(), name='animal_detail'),
]