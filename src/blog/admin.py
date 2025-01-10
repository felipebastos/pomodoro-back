from django.contrib import admin

from blog.models import Postagem


@admin.action(description="Tornar as postagens públicas")
def tornar_publicado(modeladmin, request, queryset):
    queryset.update(publicado=True)


class PostagemAdmin(admin.ModelAdmin):
    list_display = ["titulo", "texto", "publicado"]
    search_fields = ["titulo", "texto"]
    list_filter = ["publicado"]
    actions = [tornar_publicado]


# Register your models here.
admin.site.register(Postagem, PostagemAdmin)
