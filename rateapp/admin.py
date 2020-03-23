from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Module, RateInfo, Professor,Results
# Register your models here.
admin.site.register(Module)
admin.site.register(RateInfo)
admin.site.register(Professor)
admin.site.register(Results)
'''
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','name','is_staff',]
admin.site.register(CustomUser, CustomUserAdmin)
'''