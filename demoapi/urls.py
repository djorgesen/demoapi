from django.conf.urls import patterns, include, url
from django.contrib import admin
from djcore.urls import GetUrls


admin.autodiscover()

urlpatterns = GetUrls()
urlpatterns.append(url(r'^admin/', include(admin.site.urls)))
