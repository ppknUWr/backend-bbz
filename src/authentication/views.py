from django.contrib import auth
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveDestroyAPIView
from authentication.serializer import UserRegistrationSerializer, UserLoginSerializer, TokenSerializer


"""
UserRegistrationAPIView
Class with function to register new user
@Param: JSON object
        {
            username: string,           *
            email: string,              
            password: string,           *
            confrim_password: string,   *
        }
            * are required
@Return: JSON object with data of new user
        example:
        {
            "id": 0,
            "username": "temp",
            "email": "",
            "date_joined": "2021-05-20T18:14:19.656609Z",
            "token": "..."
        }
"""
class UserRegistrationAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    """
    POST request
    Creates user with given details
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)

        user = serializer.instance
        token = Token.objects.get_or_create(user = user)
        data = serializer.data
        data["token"] = token.key

        headers = self.get_success_headers(serializer.data)
        return Response(data, status = status.HTTP_201_CREATED, headers = headers)


"""
UserLoginAPIView
Class with function to login user and return token
@Param: JSON object
        username: string,          
        password: string,
@Return: JSON object with data of new user
        example:
        {
            "auth_token": "...",
            "created": "2021-05-20T18:14:19.789255Z"
        }
"""
class UserLoginAPIView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserLoginSerializer

    """
    POST request
    Returns JSON object with data of new user
    """
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = Token.objects.get_or_create(user = user)
            return Response(
                data = TokenSerializer(token).data,
                status = status.HTTP_200_OK,
            )
        else:
            return Response(
                data = serializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
            )



"""
UserTokenAPIView
Authentication with token
@Param: To pass authentication request has to have
    "Authentication": "Token ..."
    in headers, ... is token of user
@Return: JSON object with token, similiar to login
        example:
        {
            "auth_token": "...",
            "created": "2021-05-20T18:14:19.789255Z"
        }
"""
class UserTokenAPIView(RetrieveDestroyAPIView):
    authentication_classes = ([TokenAuthentication])
    permission_classes = ([IsAuthenticated])
    serializer_class = TokenSerializer
    queryset = Token.objects.all()

    """
    POST request
    Returns JSON object with token
    """
    def retrieve(self, request, *args, **kwargs):
        instance = Token.objects.get(key = request.auth.key)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

