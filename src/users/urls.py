from django.urls import path, include
from rest_framework_nested import routers
from .views import UserViewSet, AssignmentViewSet

router = routers.SimpleRouter()
router.register(r'', UserViewSet)

assignment_router = routers.NestedSimpleRouter(router, r'', lookup='list')
assignment_router.register(r'assignments', AssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'', include(assignment_router.urls)),
]
