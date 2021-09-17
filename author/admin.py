from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomUser
# Register your models here.

User = get_user_model()
# admin.site.register(Author)
# admin.site.register(Reader)
admin.site.register(User)