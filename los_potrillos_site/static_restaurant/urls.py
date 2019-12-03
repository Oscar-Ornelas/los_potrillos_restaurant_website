from django.conf.urls import url
from static_restaurant import views

app_name = 'static_restaurant'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name = 'index'),
    url(r'^menu/$', views.Menu.as_view(), name = 'menu'),
    url(r'^location/$', views.Location.as_view(), name = 'location'),
    url(r'^contact/$', views.contact_form, name = 'contact_form')
]
