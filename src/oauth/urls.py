from django.urls import path

from .views import GithubLoginView

urlpatterns = [
    path('', GithubLoginView.as_view())
]