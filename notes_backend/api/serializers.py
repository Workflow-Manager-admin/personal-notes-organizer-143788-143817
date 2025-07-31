from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for Note objects."""

    class Meta:
        model = Note
        read_only_fields = ("id", "created_at", "updated_at", "user")
        fields = read_only_fields + ("title", "content")
