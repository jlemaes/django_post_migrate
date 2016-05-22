from django.test import TransactionTestCase
from django.core.management import call_command


class TestPostMigrate(TransactionTestCase):
    def setUp(self):
        call_command('migrate', 'test_post_migrate')

    def test(self):
        call_command('migrate', 'test_post_migrate', '0001')
        call_command('migrate', 'test_post_migrate', '0002')
