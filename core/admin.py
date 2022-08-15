from django.contrib import admin
from .models import Movimentacao
# Register your models here.

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['uuid', 'valor', 'tipo', 'usuario']
    exclude = ['deleted_at',]
    readonly_fields = ['uuid']