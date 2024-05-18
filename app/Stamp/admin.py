from django.contrib import admin

from .models import (
    PatternStamp,
    Forme,
    Monture,
    Type,
    Encrier,
    PaieAccount,
    Type_account,
    Paiement,
    Commande)
# Register your models here.

admin.site.register(PatternStamp)
admin.site.register(Forme)
admin.site.register(Monture)
admin.site.register(Type)
admin.site.register(Encrier)
admin.site.register(PaieAccount)
admin.site.register(Type_account)
admin.site.register(Paiement)
admin.site.register(Commande)
