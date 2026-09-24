from django.urls import path
from . import views

app_name = 'sport_app'

urlpatterns = [
    path('', views.index, name='index'),

    # Тренеры
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('trainers/add/', views.trainer_create, name='trainer_create'),
    path('trainers/<int:pk>/', views.trainer_detail, name='trainer_detail'),
    path('trainers/<int:pk>/edit/', views.trainer_update, name='trainer_update'),
    path('trainers/<int:pk>/delete/', views.trainer_delete, name='trainer_delete'),

    # Секции
    path('sections/', views.section_list, name='section_list'),
    path('sections/add/', views.section_create, name='section_create'),
    path('sections/<int:pk>/', views.section_detail, name='section_detail'),
    path('sections/<int:pk>/edit/', views.section_update, name='section_update'),
    path('sections/<int:pk>/delete/', views.section_delete, name='section_delete'),

    # Спортсмены
    path('athletes/', views.athlete_list, name='athlete_list'),
    path('athletes/add/', views.athlete_create, name='athlete_create'),
    path('athletes/<int:pk>/', views.athlete_detail, name='athlete_detail'),
    path('athletes/<int:pk>/edit/', views.athlete_update, name='athlete_update'),
    path('athletes/<int:pk>/delete/', views.athlete_delete, name='athlete_delete'),

    # Расписание
    path('schedule/', views.schedule_list, name='schedule_list'),
    path('schedule/add/', views.schedule_create, name='schedule_create'),
    path('schedule/<int:pk>/', views.schedule_detail, name='schedule_detail'),
    path('schedule/<int:pk>/edit/', views.schedule_update, name='schedule_update'),
    path('schedule/<int:pk>/delete/', views.schedule_delete, name='schedule_delete'),

    # Абонементы
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('subscriptions/add/', views.subscription_create, name='subscription_create'),
    path('subscriptions/<int:pk>/', views.subscription_detail, name='subscription_detail'),
    path('subscriptions/<int:pk>/edit/', views.subscription_update, name='subscription_update'),
    path('subscriptions/<int:pk>/delete/', views.subscription_delete, name='subscription_delete'),
]