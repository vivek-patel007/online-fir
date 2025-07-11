from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from home.models import CustomUser,contactUs,feedback

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_user', 'is_police', 'gender','dob', 'address','city','contact_no')
        }),
        ('Police Station info', {
            'fields': ('division', 'website')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)
@admin.register(contactUs)
class contactUsAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject", "msg", "timestamp")

@admin.register(feedback)
class feedbackAdmin(admin.ModelAdmin):
    list_display = ("feedback_id", "email_id", "message", "timestamp")
