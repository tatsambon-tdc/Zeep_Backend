"""les Mapping des url de l'app PatternStamp """
from django.urls import (
                         path,
                         include
                         )
from rest_framework.routers import DefaultRouter

from Stamp import views

router = DefaultRouter()
router.register('PatternStamp', views.PatternStampViewSet)

app_name = "Stamp"

urlpatterns = [
    path('', include(router.urls)),
]
