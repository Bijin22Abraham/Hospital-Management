

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, PatientRecord

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('user_type',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'user_type', 'password1', 'password2'),
        }),
    )

class PatientRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'diagnosis', 'prescription', 'created_at')
    search_fields = ('patient__username', 'doctor__username', 'diagnosis', 'prescription')
    list_filter = ('patient__user_type', 'doctor__user_type')
    raw_id_fields = ('patient', 'doctor')  

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PatientRecord, PatientRecordAdmin)
