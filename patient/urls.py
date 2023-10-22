from django.urls import path
from patient import views 


urlpatterns=[
    path('patient-auth', views.auth, name='index'),
]