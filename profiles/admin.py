from django.contrib import admin
from .models import Posts, UserAccount, UserAccountManager
# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_admin')
admin.site.register(Posts)
admin.site.register(UserAccount)
