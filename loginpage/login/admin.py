from django.contrib import admin

# Register your models here.
from .models import log
from import_export.admin import ImportExportModelAdmin

@admin.register(log)
class ViewAdmin(ImportExportModelAdmin):
    pass
