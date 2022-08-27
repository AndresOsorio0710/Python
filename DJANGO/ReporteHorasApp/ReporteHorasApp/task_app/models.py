from tkinter import FALSE
from uuid import uuid4

from django.db import models

type = [
    ("PRIORITARY", "PRIORITARY"),
    ("INIT", "INIT"),
    ("END", "END")
]

# Create your models here.
class Task(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField('Name',max_length=50,blank=False,null=False)
    description = models.TextField('Description',blank=False,null=False )
    type = models.CharField('Type', max_length=10, blank=False, null=False, choices=type)
    

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['name']

    
    def __str__(self):
        return self.name
