from django.urls import path
from . import views
urlpatterns = [

    path('', views.home.as_view(),name='home'),
    path('add', views.add,name='add'),
    path('display', views.display,name='display'),
]