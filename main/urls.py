from django.urls import path
from . import views
from patient import views as patient_views


urlpatterns=[
    path('',views.home,name='home'),
]