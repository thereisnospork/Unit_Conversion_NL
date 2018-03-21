from django.urls import path
from convert_app.views import ListUnits
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', ListUnits.as_view()),
]