from django.urls import path
from . import views
from . import main

urlpatterns = [
    path('api/', views.show_map),
    # path('api/fetch_users', main.fetch_users)
]