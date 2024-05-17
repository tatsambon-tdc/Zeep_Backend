"""Model de l'app Stamp"""

from django.db import models
from django.conf import settings


class Forme(models.Model):
    forme = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.forme


class PatternStamp(models.Model):
    """Model PatternStamp"""

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    id = models.AutoField(primary_key=True)

    titre = models.CharField(max_length=255,
                             unique=True)

    forme = models.ForeignKey(
        Forme,
        on_delete=models.CASCADE,
        )

    prix = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # image_example = models.ImageField(upload_to=
    # 'MEDIA/image_example/PatternStamp',blank=False,null=False)
