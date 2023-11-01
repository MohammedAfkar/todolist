# from django.contrib import admin

# # Register your models here.

# from . models import todo_text

# admin.site.register(todo_text)
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Task)
