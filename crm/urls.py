from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeViewSet,
    LeaveRequestViewSet,
    ApprovalRequestViewSet,
    ProjectViewSet,
)

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"leave_requests", LeaveRequestViewSet)
router.register(r"approval_requests", ApprovalRequestViewSet)
router.register(r"projects", ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
