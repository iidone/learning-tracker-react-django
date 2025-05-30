from django.contrib import admin
from .models import Users, Ideas

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'username',
                    'name',
                    'last_name',
                    'created_at')

admin.site.register(Users, UsersAdmin)
admin.site.register(Ideas)