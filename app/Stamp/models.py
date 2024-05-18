"""Model de l'app Stamp"""

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


def validate_unique_field(value):
    # Your custom logic to check uniqueness (e.g., database query)
    if Type.objects.filter(type=value).exists():
        raise ValidationError("This value is already taken.")


class Forme(models.Model):
    """Les differentes formes (Rond,carré...)"""
    forme = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.forme


class Type(models.Model):
    """Les differentes matierie (bois,metamique...)"""
    type = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.type


class Type_account(models.Model):
    """Les differentes matierie (bois,metamique...)"""
    type = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.type


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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # image_example = models.ImageField(upload_to=
    # 'MEDIA/image_example/PatternStamp',blank=False,null=False)


class Monture(models.Model):
    """Model Monture"""

    prix = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    forme = models.ForeignKey(
        Forme,
        on_delete=models.CASCADE,
        )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )


class Encrier(models.Model):
    """Model Encrier"""

    couleur = models.CharField(max_length=255)
    disponible = models.BooleanField(default=False)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )


class PaieAccount(models.Model):
    type = models.ForeignKey(Type_account, on_delete=models.CASCADE)
    val = models.DecimalField(max_digits=20, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )


class Paiement(models.Model):
    id_PaiementAccount = models.ForeignKey(PaieAccount,
                                           on_delete=models.CASCADE)
    id_User = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    etat = models.BooleanField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    val = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Commande(models.Model):
    """Pour les commandes de cachet"""
    id = models.AutoField(primary_key=True)
    id_User = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    monture = models.ForeignKey(Monture, on_delete=models.CASCADE)
    paiement = models.ForeignKey(Paiement, on_delete=models.CASCADE)
    id_Encrier = models.ForeignKey(Encrier, on_delete=models.CASCADE)
    patternStamp = models.ForeignKey(PatternStamp, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    etat = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    ContenuStamp = models.CharField(max_length=1024)
