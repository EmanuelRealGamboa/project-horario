from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import User, Teacher

class UserAdminForm(forms.ModelForm):
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        required=False,
        help_text="Si deseas cambiar la contraseña, introdúcela aquí."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'institution_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ('username', 'email', 'role', 'institution_name', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('role',)
    readonly_fields = ('created_at',)

    fieldsets = (
        (_("Información personal"), {
            'fields': ('username', 'email', 'role', 'institution_name')
        }),
        (_("Contraseña"), {
            'fields': ('password',)
        }),
        (_("Metadatos"), {
            'fields': ('created_at',)
        }),
    )

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'institution_name')
    search_fields = ('user__username', 'user__email')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = "Nombre de usuario"

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = "Correo electrónico"
