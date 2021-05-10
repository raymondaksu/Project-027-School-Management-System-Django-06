from django.urls import path

from .views import GithubCodeView

urlpatterns = [
    path('', GithubCodeView.as_view())
]