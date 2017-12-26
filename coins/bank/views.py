from django.db import transaction
from django.db import IntegrityError
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from coins.bank.models import Account, Payment
from coins.bank.serializers import AccountSerializer, PaymentSerializer

INCOMING = "incoming"
OUTGOING = "outgoing"


class AccountViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint allows get list of accounts.

    Allowed methods: GET.

    list:
    Return a list of all accounts.
    """

    serializer_class = AccountSerializer

    def list(self, request):
        queryset = Account.objects.all()
        serializer = AccountSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class PaymentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint allows get list of payments or create payments.

    Allowed methods: GET, POST.

    list:
    Return a list of all payments.

    create:
    Create a new payment.
    Data: {"from_account": "bob123", "to_account": "alice456", "amount", 100}
    """

    serializer_class = PaymentSerializer

    def list(self, request):
        queryset = Payment.objects.all()
        serializer = PaymentSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        try:
            with transaction.atomic():
                from_account = Account.objects.select_for_update().get(id=request.data['from_account'])
                to_account = Account.objects.select_for_update().get(id=request.data['to_account'])
                from_account.balance = from_account.balance - Decimal(request.data['amount'])
                to_account.balance = to_account.balance + Decimal(request.data['amount'])
                Payment.objects.create(account=from_account, to_account=to_account, amount=request.data['amount'], direction=OUTGOING)
                Payment.objects.create(account=to_account, from_account=from_account, amount=request.data['amount'], direction=INCOMING)
                from_account.save()
                to_account.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
