from django.contrib import admin

from dynamic.models import Branch, Pages, Quote

from django.contrib.auth.models import User, Group


# Register your models here.
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'mobile', 'email']
    ordering = ['name']
    list_filter = ['category', 'mobile']


class CitypageADMIN(admin.ModelAdmin):
    list_display = ['city', 'title']
    ordering = ['city']


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 's_from', 's_to', 'date', 'email', 'message', 'reviewed']
    list_editable = ['reviewed']
    list_filter = ['reviewed']
    ordering = ['reviewed']


admin.site.register(Branch, BranchAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Pages, CitypageADMIN)

admin.site.unregister(User)
admin.site.unregister(Group)