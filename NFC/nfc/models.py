"""Custom model definitions for the NFC plugin.

This file is where you can define any custom database models.

- Any models defined here will require database migrations to be created.
- Don't forget to register your models in the admin interface if needed!
"""

from django.db import models


class NFCTagLink(models.Model):
    """Maps an NFC tag UID to an InvenTree Part"""

    uid = models.CharField(max_length=64, unique=True, verbose_name="NFC Tag UID")

    part = models.ForeignKey(
        "part.Part",
        on_delete=models.CASCADE,
        related_name="nfc_tags",
        verbose_name="Linked Part",
    )

    linked_at = models.DateTimeField(auto_now_add=True)

    linked_by = models.ForeignKey(
        "auth.User", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        app_label = "nfc"

    def __str__(self):
        return f"NFC {self.uid} : {self.part.name}"
