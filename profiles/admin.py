from django.contrib import admin
from models import Posts, UserAccount, UserAccountManager
# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'created_at', 'is_admin', 'deactivated')
admin.site.register(Posts)
