from django.urls import path
from . import views

urlpatterns = [
    path('api/v1', views.author_list),
    path('api/v1/<int:pk>', views.snippet_detail)
]