from django.contrib import admin

from .models import Gr1



# Register your models here.
class GrAdmin(admin.ModelAdmin):
    pass   


admin.site.register(Gr1, GrAdmin)