from django.urls import path
from . import views


urlpatterns = [
    path('', views.coreOverview, name="core-overview"),
    path('task-list/', views.tasklist, name="task-list"),
]