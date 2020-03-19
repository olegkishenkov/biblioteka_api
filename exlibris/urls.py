from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'biographies', views.BiographyViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'readers', views.ReaderViewSet)
router.register(r'lends', views.LendViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('authors_functions', views.author_list, name='authors_functions'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]