from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator

# Create your models here.
class Puzzle(models.Model):
    int_list = models.CharField(validators=[int_list_validator], max_length=100, default='0')
    player = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    
