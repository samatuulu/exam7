"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from questiona.views import PollListView, PollDetailView, PollCreateView, PollUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollListView.as_view(), name='poll'),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    path('poll/create/', PollCreateView.as_view(), name='poll_create'),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name='poll_update'),
]
