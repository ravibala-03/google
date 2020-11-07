from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from searchapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url('search/', include('searchapp.urls')),
]

