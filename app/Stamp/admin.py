from django.contrib import admin

from .models import PatternStamp, Forme, Monture, Type, Encrier
# Register your models here.

admin.site.register(PatternStamp)
admin.site.register(Forme)
admin.site.register(Monture)
admin.site.register(Type)
admin.site.register(Encrier)
