from django.db import models

# Create your models here.
# Son pequeñas clases que nos van a generar objetos para trabajar dentro del proyecto.


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Categoria")
    image = models.ImageField(
        default="null", verbose_name="Imagen", upload_to="articles"
    )
    public = models.BooleanField(verbose_name="Publico")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    # La clase meta nos permite configurar un modelo a nivel de funcionamient interno
    # Criterio de ordenacion, nombre, etc..
    class Meta:
        ordering = ["-created_at"]  # ordena los articulos como queramos
        verbose_name = "Artículo"  # Nombre legible del modelo
        verbose_name_plural = "Artículos"  # Nombre legible del modelo
        # db_table = "articles_table"   # Nombre de la tabla en la base de datos

    # Cambiamos el nombre por defecto que nos aparece en el panel de admin (Article object(id))
    def __str__(self):
        if self.public:
            public = "(Public)"
        else:
            public = "(Private)"
        return f"{self.title} {public}"


class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = "Categoria"  # Nombre legible del modelo
        verbose_name_plural = "Categorias"  # Nombre legible del modelo
