from django.contrib import admin

# Register your models here.
from web.models import UserAction


@admin.register(UserAction)
class AdminUserAction(admin.ModelAdmin):
    list_display = ['email', 'ip', 'get_country_code_display', 'timestamp']
    list_filter = ['country_code']
    date_hierarchy = 'timestamp'
    search_fields = ['email', 'ip']
    search_help_text = ['Поиск по емайл или IP']