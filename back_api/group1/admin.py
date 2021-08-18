from django.contrib import admin
from .models import Group1


# Register your models here.
class Group1Admin(admin.ModelAdmin):
    pass


admin.site.register(Group1, Group1Admin)
