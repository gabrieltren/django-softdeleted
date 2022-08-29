from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["titulo", "uuid", "criado_em", "atualizado_em", "deletado_em"]
    readonly_fields = ["uuid",]
    exclude = ["deletado_em",]