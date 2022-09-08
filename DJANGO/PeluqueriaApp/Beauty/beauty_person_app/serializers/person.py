from beauty_person_app.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ['id']


class ListPersonSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    date_of_birth = serializers.DateField()
    gender = serializers.CharField()


class SavePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["first_name","last_name","email","phone_number","gender","date_of_birth"]
    
    def validate(self, attrs):
        attrs.update({
            'first_name': attrs.get('first_name').upper(),
            'last_name': attrs.get('last_name').upper()
        })
        return attrs