from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Subscription, Store
from .serializers import SubscriptionSerializer, StoreSerializer


class StoreList(APIView):

    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetail(APIView):

    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        store = self.get_object(pk)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        store = self.get_object(pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriptionList(APIView):

    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionDetail(APIView):

    def get_object(self, pk):
        try:
            return Subscription.objects.get(pk=pk)
        except Subscription.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subscription = self.get_object(pk)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
