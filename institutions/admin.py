from django.contrib import admin
from .models import Institution, Group

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'responsible', 'type')
    search_fields = ('name', 'email')
    list_filter = ('type',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'institution')  
    list_filter = ('grade', 'institution')
