from django.contrib import admin


from .models import Gr
from .models import GrSort
from .models import GrFile

# Register your models here.
class GrAdmin(admin.ModelAdmin):
    pass   
# Register your models here.
class GrSortAdmin(admin.ModelAdmin):
    pass

class GrFileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gr, GrAdmin)
admin.site.register(GrSort, GrSortAdmin)
admin.site.register(GrFile, GrFileAdmin)
