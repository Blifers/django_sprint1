from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about', views.about, name='pages_about'),
    path('rules/', views.rules, name='pages_rules'),
]
