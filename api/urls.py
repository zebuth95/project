from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .viewsets import Test_One, UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet, GetAuthToken, current_user

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('task', TaskViewSet)
router.register('comment', CommentViewSet)
router.register('project', ProjectViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('test/', Test_One.as_view()),
    path('current_user/', current_user)
]
