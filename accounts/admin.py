from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CandidateProfile, EmployerProfile

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'role', 'is_verified', 'is_staff')
    list_filter = ('role', 'is_verified', 'is_staff', 'is_active')
    
    # Expose custom fields inside the dashboard view wrapper
    fieldsets = UserAdmin.fieldsets + (
        ('Role Configuration', {'fields': ('role', 'is_verified', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Configuration', {'fields': ('role', 'is_verified', 'phone')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(CandidateProfile)
admin.site.register(EmployerProfile)