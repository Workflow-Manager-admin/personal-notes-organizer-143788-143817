from django.db import models
from django.contrib.auth import get_user_model


class Note(models.Model):
    """
    Represents a single user note.

    Each note is owned by a user and contains a title and free-form text
    content.  Timestamps are automatically captured for auditing.
    """
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="notes",
        help_text="Owner of the note"
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated_at",)

    # PUBLIC_INTERFACE
    def __str__(self) -> str:
        """Return a readable representation of the note."""
        return f"{self.title} (id={self.pk})"
