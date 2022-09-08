from dataclasses import fields
from django.forms import ModelForm
from beauty_person_app.models import Person


class PersonForm(ModelForm):
    class Meta:
        models = Person
        fields = ["first_name","last_name","email","phone_number","gender","date_of_birth"]