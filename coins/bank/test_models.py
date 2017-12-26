"""
Unittests for Bank models.
"""

from django.test import TestCase
from coins.bank.models import Account, Payment
from coins.bank.views import INCOMING, OUTGOING


class AccountTestCase(TestCase):
    """
    Test Account model.
    """
    def setUp(self):
        Account.objects.create(id="test11", owner="test1", balance=10, currency="PHP")
        Account.objects.create(id="test21", owner="test2", balance=10, currency="PHP")

    def test_accounts_created(self):
        """Check that acounts was created"""
        test1 = Account.objects.get(id="test11")
        test2 = Account.objects.get(id="test21")
        self.assertEqual(test1.id, "test11")
        self.assertEqual(test2.id, "test21")


class PaymentTestCase(TestCase):
    """
    Test Payment model.
    """
    def setUp(self):
        test1 = Account.objects.create(id="test11", owner="test1", balance=10, currency="PHP")
        test2 = Account.objects.create(id="test21", owner="test2", balance=10, currency="PHP")
        Payment.objects.create(account=test1, to_account=test2, amount=1, direction=OUTGOING)
        Payment.objects.create(account=test2, from_account=test1, amount=1, direction=INCOMING)

    def test_accounts_created(self):
        """Check that payments was created"""
        test1 = Payment.objects.get(account="test11")
        test2 = Payment.objects.get(account="test21")
        a_test1 = Account.objects.get(id="test11")
        a_test2 = Account.objects.get(id="test21")
        self.assertEqual(test1.to_account, a_test2)
        self.assertEqual(test1.direction, OUTGOING)
        self.assertEqual(test2.direction, INCOMING)
