from django.contrib import admin
# from .forms import SimpleUserForm, SimpleUserChangeForm
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# class CustomizedAdmin(UserAdmin):
#     add_form = SimpleUserForm
#     form = SimpleUserChangeForm
#     model = SimpleUser
#     list_display = ['email', 'username', 'user_avatar', 'user_phone_num']
#
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('user_avatar',)}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('user_avatar','user_phone_num',)}),
#     )

admin.site.register(SimpleUser)
# admin.site.register(SimpleUser, CustomizedAdmin)
