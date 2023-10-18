from django.db import models

# Create your models here.

class todo_text(models.Model):
    text = models.CharField(max_length=100)
