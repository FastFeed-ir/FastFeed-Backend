from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BusinessOwner
from .serializers import BusinessOwnerSerializer

class BusinessOwnerList(APIView):
    def get(self, request):
        business_owners = BusinessOwner.objects.all()
        serializer = BusinessOwnerSerializer(business_owners, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BusinessOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessOwnerDetail(APIView):
    def get_object(self, pk):
        try:
            return BusinessOwner.objects.get(pk=pk)
        except BusinessOwner.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        business_owner = self.get_object(pk)
        serializer = BusinessOwnerSerializer(business_owner)
        return Response(serializer.data)

    def put(self, request, pk):
        business_owner = self.get_object(pk)
        serializer = BusinessOwnerSerializer(business_owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        business_owner = self.get_object(pk)
        business_owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
