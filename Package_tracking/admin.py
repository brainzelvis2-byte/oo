from django.contrib import admin
from .models import Package, PackageDetails
# Register your models here.

admin.site.register(PackageDetails)
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'receiver_name', 'status', 'created_at')
    list_editable = ('status',)
    list_filter = ('status', 'created_at')
