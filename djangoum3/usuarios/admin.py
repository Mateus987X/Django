from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioChangeForm, CustomUsuarioCreateForm
from .models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ("first_name", "last_name", "email", "fone", "is_staff")

    add_fieldsets = (
        (None,{"classes": ("wide",),"fields": ("username", "password1", "password2"),},),
        ("Informacoes Pessoais", {"fields": ("first_name", "last_name", "fone")}),
        ("Permissoes", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Datas Importantes", {"fields": ("last_login", "date_joined")}),
    )

    # fieldsets = (
    #     (None, {"fields": ("email", "password")}),
    #     ("Informacoes Pessoais", {"fields": ("first_name", "last_name", "fone")}),
    #     ("Permissoes", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    #     ("Datas Importantes", {"fields": ("last_login", "date_joined")}),
    # )
