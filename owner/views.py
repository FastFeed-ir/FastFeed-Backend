# from requests import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import BusinessOwner
from .serializers import BusinessOwnerSerializer


class BusinessOwnerViewSet(ModelViewSet):
    queryset = BusinessOwner.objects.all()
    serializer_class = BusinessOwnerSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ('phone_number',)
    ordering_fields = '__all__'

    # @staticmethod
    # def login(request):
    #     # Get the username and password from the request
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #
    #     # Find the user with the provided username and password
    #     user = BusinessOwner.objects.get(username=username, password=password)
    #
    #     # Generate a new verification code
    #     user.verification_code = user.generate_verification_code()
    #     user.save()
    #
    #     # Send the verification code via SMS
    #     user.send_verification_sms()
    #
    #     return Response({'success': True})
