from django.urls import path, include
from rest_framework_nested import routers
from .views import UserViewSet, SubmissionsViewSet, CustomAuthToken, UserProfileView

router = routers.SimpleRouter()
router.register(r'', UserViewSet)

assignment_router = routers.NestedSimpleRouter(router, r'', lookup='list')
assignment_router.register(r'submissions', SubmissionsViewSet, basename='submissions')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='user-profile'),
    path('', include(assignment_router.urls)),
    path('login', CustomAuthToken.as_view())
]
