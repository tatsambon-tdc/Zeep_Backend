"""
Commande  pour attendre que le service de la BD
soi lancer et que la BD est disponible
"""


import time
from psycopg2 import OperationalError as Psycopg2Error

# pour traque les erreurs liées à la bd
from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Commande Django Pour l'attente de la BD"""

    def handle(self, *args, **options):
        self.stdout.write('En attente de la base de donné')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("la bd n'est pas encore disponible ,\
                                  Patientez 1 seconde...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS(
            "Base de Donnée disponible  !:)"
            ))
