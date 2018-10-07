from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from Transaction.models import Transaction
from Transaction.serializer import TransactionSerializer


class TransactionList(generics.ListCreateAPIView):
    """List all transactions or create a new transaction"""

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, format=None):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a transaction"""

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_transaction(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transaction = self.get_transaction(pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        prev_transaction = self.get_transaction(pk)
        serializer = TransactionSerializer(prev_transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
