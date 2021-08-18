from django.contrib import admin
from .models import Group2


# Register your models here.
class Group2Admin(admin.ModelAdmin):
    pass


admin.site.register(Group2, Group2Admin)
