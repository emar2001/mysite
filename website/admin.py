from django.contrib import admin
from website.models import contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')




admin.site.register(contact, ContactAdmin)