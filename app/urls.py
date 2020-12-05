from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.serverstate, name='serverstate'),
    path('list/', views.NPoemRanksListAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
