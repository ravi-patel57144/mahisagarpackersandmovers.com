from django.contrib import admin

from dynamic.models import Branch, Pages, Quote


# Register your models here.
class BranchAdmin(admin.ModelAdmin):
    list_display =['name', 'address', 'mobile', 'email']

class CitypageADMIN(admin.ModelAdmin):
    list_display = ['city', 'title']


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 's_from', 's_to', 'date', 'email', 'message', 'reviewed']
    list_editable = ['reviewed']
    list_filter = ['reviewed']


admin.site.register(Branch, BranchAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Pages, CitypageADMIN)