from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from . import models
# Create your views here.

@api_view(['POST'])
def register_view(request):
    print("req",request.data)
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            acount = serializer.save()
            acount.set_password(acount.password)
            acount.save()
            token, _ = Token.objects.get_or_create(user=acount)
            data = serializer.data
            data['token'] = token.key
            data["user_id"] = acount.id
            data["joined_at"] = acount.date_joined
        else:
            data = serializer.errors
        return Response(data)

    # def create(self, validated_data):
    #     user= User.objects.create(username=validated_data['username'],email = validated_data['email'])
    #     user.set_password(validated_data['password'])
    #     user.save()

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):

        print(request.data)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
    
        return Response({
            'token': token.key,
            'user_id': user.pk, 
            'email': user.email,
            "username":user.username,
            "joined_at": user.date_joined
        })

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
            'message': 'logout, token deleted'
        }
        return Response(data)