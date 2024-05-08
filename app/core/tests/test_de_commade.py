"""
Test des commandes Django De management  personalisées ;
"""

# simuler le service de la bd
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

# pour l'appele de commande à tester
from django.core.management import call_command

# pour traque les erreurs liées à la bd
from django.db.utils import OperationalError

# vu que il n'y pas besoin d'applique des migrations du au test
from django.test import SimpleTestCase


@patch('core.management.commands.attente_de_la_bd.Command.check')
# vu que la commande a simuler c'est celle  envoyée en parametre
class CommadeTests(SimpleTestCase):
    """Test d'attente de la bd"""

    def test_attente_de_la_bd(self, patched_check):
        # patched_check vient
        # de la simulation effectuée grace
        # au decorateur @patch
        """Test d'attente si la bd est disponible ."""

        patched_check.return_value = False

        call_command('attente_de_la_bd')

        patched_check.asser_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Teste de l'attente effective en cas de  OperationalError"""

        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('attente_de_la_bd')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
