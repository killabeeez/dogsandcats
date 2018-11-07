from django.conf.urls import url
from pets import views

urlpatterns = [
    url(r'^list/$', views.PetsView.as_view()),
    url(r'^list/(?P<pk>[0-9]+)/$', views.PetDetails.as_view()),

]

