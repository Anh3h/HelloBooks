from rest_framework import serializers

from Transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'user', 'book', 'date', 'status')
