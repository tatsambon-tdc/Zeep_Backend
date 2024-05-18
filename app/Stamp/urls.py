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

router2.register('PatternStamp',
                 views.AdminPatternStampViewSet,
                 basename="adminPatternStamp"
                 )

router2.register('Monture',
                 views.AdminMontureViewSet,
                 basename="adminMonture"
                 )


app_name = "Stamp"

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", include(router2.urls))
]
