from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('add-question', views.question_add, name='question_add'),
    path('accounts/profile/', views.profile, name='profile'),
    path('questions/add-question', views.question_add, name='question_add'),
    path('questions/', views.index, name='index'),

]