from rest_framework import routers
from django.conf.urls import url, include
from invite2app.api import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^friends/', views.FacebookFriends.as_view(), name='friends'),
    url(r'^friends_inside', views.FriendsUsingApp.as_view(),
        name='friends_inside'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
    ]
