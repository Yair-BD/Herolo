"""heroloapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
urlpatterns = [
    path("", apiOverView, name="api-overview"),
    path("list-message", all_messages, name="list-message"),
    path("write-message", write_message, name="write-message"),
    path("unread-message", all_unread_message, name="unread-message"),
    path("read-message/<str:pk>/", read_message, name="read-message"),
    path("delete-message/<str:pk>/", delete_message, name="delete-message")
]