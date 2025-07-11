from django.contrib import admin
from userfir.models import missingPerson,FIR,criminal
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
@admin.register(missingPerson)
class missingPersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "city", "address","mobile_no","image_tag", "timestamp")
    readonly_fields = ['image_tag']
class ImageInline(GenericTabularInline):
    model = [missingPerson,criminal]
@admin.register(FIR)
class FIRAdmin(admin.ModelAdmin):
    list_display = ("police_station", "complaint_type", "image_tag", "timestamp")
    readonly_fields = ['image_tag']

@admin.register(criminal)
class criminalAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "contact_no", "address","image_tag","timestamp")
    readonly_fields = ['image_tag']

