from django.db import models
from django_paranoid.models import ParanoidModel
from django.forms import ValidationError
from uuid import uuid4

genders = [
    ("FEMALE","FEMALE"),
    ("MALE","MALE"),
    ("OTHER","OTHER"),
    ("NOT SUPPLIED","NOT SUPPLIED")
]


def validate_gender(value):
    try:
        index = genders.index(value)
    except:
        raise ValidationError('This valur is not allowed.')


def only_numbers(value):
    if value.isdigit() == False:
        raise ValidationError('This fiels only allows numbers.')


class Person(ParanoidModel):
    id = models.UUIDField('ID', default=uuid4, editable=False, primary_key=True)
    first_name = models.CharField('Firts name', max_length=50, blank=False, null=False)
    last_name = models.CharField('Last name', max_length=50, blank=False, null=False)
    email = models.EmailField('Email', blank=False, null=False, unique=True)
    phone_number = models.CharField('Phone number', max_length=16, blank=False, null=False, unique=True, validators=[only_numbers])
    date_of_birth = models.DateField('Date of birth', blank=False, null=False)
    gender = models.CharField('Gender', max_length=15, choices=genders)
    is_user = models.BooleanField('Is User', default=False)

    
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = ['last_name','first_name']
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'.upper
