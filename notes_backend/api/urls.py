from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteViewSet, health

router = DefaultRouter()
router.register(r"notes", NoteViewSet, basename="note")

urlpatterns = [
    path("health/", health, name="Health"),
    path("", include(router.urls)),
]
