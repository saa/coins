from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from coins.bank.views import AccountViewSet, PaymentViewSet
from coins.bank.models import Account, Payment


class AccountViewSet(APITestCase):
    """
    Create two test users and get list of accounts
    """
    def setUp(self):
        Account.objects.create(id="test31", owner="test3", balance=10, currency="PHP")
        Account.objects.create(id="test41", owner="test4", balance=10, currency="PHP")

    def test_get_list_of_accounts(self):
        """
        Get list of accounts, check that status is 200.
        """
        url = reverse('account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Account.objects.count())


class PaymentViewSet(APITestCase):
    """
    Create two test users, create payment and get list of payments.
    Also try get 400 with wrong amount.
    """
    def setUp(self):
        Account.objects.create(id="test51", owner="test5", balance=10, currency="PHP")
        Account.objects.create(id="test61", owner="test6", balance=10, currency="PHP")

    def test_create_payment(self):
        """
        Create payment from account test51 to test61.
        """
        url = reverse('payment-list')
        data = {"from_account": "test51", "to_account": "test61", "amount": 0.3}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        test5 = Account.objects.get(id="test51")
        test6 = Account.objects.get(id="test61")
        self.assertEqual(float(test5.balance), 9.7)
        self.assertEqual(float(test6.balance), 10.3)

    def test_400_if_amount_wrong(self):
        """
        Test that if amount is wrong API return 400 and balance is ok.
        """
        url = reverse('payment-list')
        data = {"from_account": "test51", "to_account": "test61", "amount": 3000}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        test5 = Account.objects.get(id="test51")
        test6 = Account.objects.get(id="test61")
        self.assertEqual(float(test5.balance), 10.0)
        self.assertEqual(float(test6.balance), 10.0)
