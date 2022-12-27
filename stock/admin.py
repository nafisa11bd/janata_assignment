from django.contrib import admin
from .models import stockinfo
from import_export import resources
from import_export.admin import ImportExportModelAdmin
class stockresource(resources.ModelResource):
    class Meta:
        model=stockinfo
class stockadmin(ImportExportModelAdmin):
    resource_class=stockresource


admin.site.register(stockinfo,stockadmin)

# Register your models here.
