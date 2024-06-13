from django.contrib import admin
from institutions.models import Institution


@admin.register(Institution)
class Institution(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city__name')
    ordering = ('city__name', 'name')