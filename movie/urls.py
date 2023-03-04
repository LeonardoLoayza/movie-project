from django.urls import path, include
from rest_framework import routers 
from . import views 

#To be able to use the MovieViewSet we need to use a router 
router = routers.DefaultRouter()
router.register('', views.MovieViewSet) 

urlpatterns = [
    path('', include(router.urls))
]


