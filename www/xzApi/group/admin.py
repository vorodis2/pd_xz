from django.contrib import admin

from .models import (
    Group,
    GroupType,
    GroupSort,
    GroupFile,
)


class GroupAdmin(admin.ModelAdmin):
    pass


class GroupTypeAdmin(admin.ModelAdmin):
    pass


class GroupFileAdmin(admin.ModelAdmin):
    pass


class GroupSortAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)
admin.site.register(GroupType, GroupTypeAdmin)
admin.site.register(GroupSort, GroupSortAdmin)
admin.site.register(GroupFile, GroupFileAdmin)
