from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on notes.

    All endpoints require authentication. A user can only access notes that
    they own.
    """
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # PUBLIC_INTERFACE
    def get_queryset(self):
        """Return notes belonging to the authenticated user."""
        return Note.objects.filter(user=self.request.user)

    # PUBLIC_INTERFACE
    def perform_create(self, serializer):
        """Attach the logged-in user to the note before saving."""
        serializer.save(user=self.request.user)


@api_view(["GET"])
def health(request):
    """Simple health-check endpoint."""
    return Response({"message": "Server is up!"})
