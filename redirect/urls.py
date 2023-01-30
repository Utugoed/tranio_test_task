from django.urls import path

from redirect import views


urlpatterns = [
    path('<str:code>/', views.get_redirect_url, name="redicrect"),
]