from django.db import models
from django.core.exceptions import ValidationError
# from django.forms import ValidationError
# Create your models here.
def check_for_a(value):
    if value[0].lower()=='a':
        raise ValidationError('Name Started with A')

def check_for_len(val):
    if len(val)<5:
        raise ValidationError('Lenght of Value id less than 5')

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,validators=[check_for_a,check_for_len])

    def __str__(self):
        return self.topic_name
