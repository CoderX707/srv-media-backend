from django.contrib import admin
from channels_api.models import Category, Channel, Subcription
# Register your models here.
admin.site.register(Category)
admin.site.register(Subcription)
admin.site.register(Channel)