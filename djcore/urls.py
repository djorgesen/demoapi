from django.conf.urls import patterns, include, url
from rest_framework import routers
from djcore import views


def GetUrls():
    router = routers.DefaultRouter()
    #router.register(r'users',views.UsersView,'users')

    urlpatterns = patterns('',
                           # Api End Points
                           url(r'^', include(router.urls)),
                           url(r'^auth/',views.obtain_jwt_token ),
                           #url(r'^token/refresh/',views.RefreshTokenView.as_view() ),
                           #url(r'^user/me/',views.SelfView.as_view()),
                           )

    return urlpatterns