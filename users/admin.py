from django.contrib import admin

from users.models import Users, UserProfiles


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name',
                    'is_active', 'is_staff', 'date_joined']
    list_display_links = ('id', 'email')
    list_filter = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']
    date_hierarchy = 'date_joined'
    ordering = ['first_name', 'last_name', 'is_active']


@admin.register(UserProfiles)
class ProfileAdmin(admin.ModelAdmin):
    pass


