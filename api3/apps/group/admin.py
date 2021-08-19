from django.contrib import admin

from .models import (
    Group,   
    GroupSort,
    GroupFile,
    GroupComment,
)

admin.site.register(GroupComment)
admin.site.register(Group)
admin.site.register(GroupSort)
admin.site.register(GroupFile)

