from django.urls import path, include

from . import views


urlpatterns = [
    path('url/', views.ListCreateUrlsView.as_view(), name="urls-list-create"),
]