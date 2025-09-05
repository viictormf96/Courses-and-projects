from django.contrib import admin
from .models import Article, Category


# Register your models here.
# Configuramos el panel para que muestre los parametros que queremos
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


# Añadimos los modelos que se veran en el panel de administracion
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configurar el titulo y el header del panel de admin
NAME = "Python Master - Victor Muntane"
admin.site.site_header = NAME
admin.site.site_title = NAME
admin.site.index_title = "Panel de Gestión"
