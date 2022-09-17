from person_app.models import Person
from rest_framework import serializers
from django.contrib.auth.models import User


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
        fields = ["first_name","last_name","email","phone_number","gender","date_of_birth","is_user"]
    
    
    def validate(self, attrs):
        if attrs.get('is_user'):
            user = User()
            user.username = attrs.get('email')
            user.first_name = attrs.get('first_name')
            user.last_name = attrs.get('last_name')
            user.email = attrs.get('email')
            user.set_password('Bt-'+attrs.get('phone_number'))
            user.save()
            print('User create success.')
        attrs.update({
            'first_name': attrs.get('first_name').upper(),
            'last_name': attrs.get('last_name').upper()
        })
        return attrs