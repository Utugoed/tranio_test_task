from django.urls import path

from shorter import views


urlpatterns = [
    path('', views.get_index_page, name="index"),
    path('create_code/', views.create_code, name="create_code"),
    path('statistic/', views.statistic, name="statistic")
]