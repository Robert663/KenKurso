from rest_framework import generics
from rest_framework.views import APIView, Response, status
from .serializers import SuperUserSerializers, UserSerializers, UpdateUserSerializers, LoginUserSerializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User


class UserAllView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_queryset(self):
        amount_user = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:amount_user]


class SuperUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializers
    

class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializers


class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginUserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"]
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status.HTTP_200_OK)

        return Response({"detail": "Invalid email or password"}, status.HTTP_401_UNAUTHORIZED)
