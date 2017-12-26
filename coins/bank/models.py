from django.db import models


class Account(models.Model):
    id = models.TextField(primary_key=True)
    owner = models.TextField()
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.TextField()

    class Meta:
        db_table = "accounts"
        db_constraints = {
            'positive_balance': 'check (balance >= 0)'
        }


class Payment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+')
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+', null=True)
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='+', null=True)
    direction = models.TextField()

    class Meta:
        db_table = "payments"
