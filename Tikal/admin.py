from django.contrib import admin
from .models import Cliente, Telefone


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('ddd', 'numero')
