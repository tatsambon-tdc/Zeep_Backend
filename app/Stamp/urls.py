"""les Mapping des url de l'app PatternStamp """
from django.urls import (
                         path,
                         include
                         )
from rest_framework.routers import SimpleRouter

from Stamp import views

router = SimpleRouter()
router2 = SimpleRouter()

router.register('PatternStamp', views.PatternStampViewSet)
router.register('Monture', views.MontureViewSet)
router.register('Encrier', views.EncrierViewSet)

router2.register('PatternStamp',
                 views.AdminPatternStampViewSet,
                 basename="adminPatternStamp"
                 )

router2.register('Monture',
                 views.AdminMontureViewSet,
                 basename="adminMonture"
                 )
router2.register('PaieAccount',
                 views.PaieAccountViewSet,
                 basename="adminPaieAccount"
                 )


router2.register('Encrier',
                 views.AdminMontureViewSet,
                 basename="adminEncrier"
                 )

router2.register('Paiement',
                 views.PaiementViewSet,
                 basename="adminPaiement"
                 )


app_name = "Stamp"

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", include(router2.urls))
]
