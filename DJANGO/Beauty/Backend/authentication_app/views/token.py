from authentication_app.serializers import TokenSerializer
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from .permissions import CustomDjangoModelPermission


@authentication_classes([TokenAuthentication])
@permission_classes([CustomDjangoModelPermission])
class TokenViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


    def get_queryset(self):
        queryset = super(TokenViewSet, self).get_queryset()
        return queryset
    
    def get_serializer_class(self):
        serializer = {
        }
        if self.action in serializer:
            return serializer[self.action]
        return TokenSerializer