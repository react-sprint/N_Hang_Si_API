from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.serverstate, name='serverstate'),
    path('ranklist/', views.NPoemRanksListAPI.as_view()),
    path('register/', views.NPoemRegisterAPI.as_view()),
    path('like/<int:pk>/increase/', views.NPoemIncreaseLikeAPI.as_view()),
    path('like/<int:pk>/decrease/', views.NPoemDecreaseLikeAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
