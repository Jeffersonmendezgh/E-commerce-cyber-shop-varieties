from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Auth


class AuthAdmin(UserAdmin):
    list_display =('email','name','lastname','username','last_join','date_joined','is_active',)
    list_display_links =('email','name','lastname')
    readonly_fields=('last_join','date_joined')
    ordering=('-date_joined',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Auth, AuthAdmin)

