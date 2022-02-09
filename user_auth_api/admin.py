from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User,UserManager
from django.contrib.auth.models import Group

admin.site.register(User)
admin.site.unregister(Group)