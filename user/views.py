from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from user.serializer import RegisUserSerializer, LoginSerializer
from user.serializer import ProfileSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import authenticate
from user.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class SignUp(generics.GenericAPIView):
    serializer_class = RegisUserSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Пользователь успешно зарегестрирован!",
                "data": serializer.data

            }

            return Response(data=response)
        return Response(data=serializer.errors)


class SignIn(APIView):
    serializer_class = LoginSerializer

    def post(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,
                            password=password)

        if user is not None:
            refresh = RefreshToken().for_user(user)
            response = {
                "Сообщение": "Вы успешно вошли в систему",
                "tokens": {"refresh": str(refresh),
                           "access": str(refresh.access_token)},
                "user": user.username
            }
            return Response(data=response)
        else:
            return Response(data={"Сообщение": "Вы не авторизованы \nЗарегестрируйтесь"})


class ProfileView(APIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        user = request.user
        return Response({'username': user.username,
                         'email': user.email,
                         })


class EditProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]



