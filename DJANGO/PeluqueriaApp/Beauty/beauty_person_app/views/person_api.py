from beauty_person_app.models import Person
from beauty_person_app.serializers import *
from rest_framework import viewsets, mixins


class PersonViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):
    queryset = Person.objects.all().order_by('last_name','first_name')
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = super(PersonViewSet, self).get_queryset()
        return queryset
    
    def get_serializer_class(self):
        serializer = {
            'create': SavePersonSerializer 
        }
        if self.action in serializer:
            return serializer[self.action]
        return PersonSerializer