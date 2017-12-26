"""
Bank serializers for Account and Payment models.
"""

from coins.bank.models import Account, Payment
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    """
    Account serializer.
    """
    class Meta:
        model = Account
        fields = ('id', 'owner', 'balance', 'currency')


class PaymentSerializer(serializers.ModelSerializer):
    """
    Payment serializer.
    """
    class Meta:
        model = Payment
        fields = ('amount', 'to_account', 'from_account')
