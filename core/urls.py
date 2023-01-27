from django.urls import path, include

from . import views


urlpatterns = [
    path('url/', views.ListCreateUrlsView.as_view(), name="urls-list-create"),
    path('url/<int:pk>/', views.UrlDetailView.as_view(), name="url-details"),
]