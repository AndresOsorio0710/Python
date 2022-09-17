from authentication_app.serializers import UserSerializer,ListUserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes,permission_classes
from .permissions import CustomDjangoModelPermission


#@authentication_classes([TokenAuthentication])
#@permission_classes([CustomDjangoModelPermission])
class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    queryset = User.objects.all().values(
            'id','username','first_name','last_name','email')
    serializer_class = UserSerializer


    def get_queryset(self):
        queryset = super(UserViewSet, self).get_queryset()
        return queryset
    
    def get_serializer_class(self):
        serializer = {
            'retrieve': ListUserSerializer
        }
        print(f'-----------------{self.action}')
        if self.action in serializer:
            return serializer[self.action]
        return UserSerializer

    @action(methods=['GET'], detail=False, url_name='key', url_path='key', name='key')
    def get_id(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)