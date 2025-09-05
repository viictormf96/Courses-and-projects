"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings

# importar app con mis vistas
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Introducimos una url en la raiz de la pagina
    path("", views.index, name="index"),
    path("home/", views.index, name="home"),
    # Introducimos una url /hello-world
    path("hello-world/", views.hello_world, name="hello_world"),
    path("contact/", views.contact, name="contact"),
    # Cremos una url con parametros dentro de esta. Podemos hacer que sean opcionales.
    path("contact/<str:name>/", views.contact, name="contact"),
    path("contact/<str:name>/<str:surname>/", views.contact, name="contact"),
    path("test-page/", views.page, name="test_page"),
    # Redirigimos la pagina a otro lado dependiendo si introducimos un valor o otro en la url
    path("test-page/<int:redirect_url>/", views.page, name="test_page"),
    # Creamos una url para crear un nuevo Articulo
    path("create-article/", views.create_article, name="create_article"),
    path(
        "create-article/<str:title>/<str:content>/<str:public>/",
        views.create_article,
        name="create_article",
    ),
    # Creamos un path para un formulario que genere un articulo
    path(
        "save-article/",
        views.save_article,
        name="save_article",
    ),
    path(
        "create-article-form/",
        views.create_article_form,
        name="create_article_form",
    ),
    # Path hacia el form creado por un objeto form
    path(
        "create-full-article/",
        views.create_full_article,
        name="create_full_article",
    ),
    # Path para mostrar un articulo de la bbdd
    path("show-article/", views.show_article, name="show_article"),
    # Path para actualizar un articulo de la bbdd
    path(
        "update-article/<int:id_article>", views.update_article, name="update_article"
    ),
    # Path para mostrar una lista de articulos
    path("articles/", views.articles_list, name="articles"),
    # Path para eliminar un articulo
    path(
        "delete-article/<int:id_article>", views.delete_article, name="delete_article"
    ),
]

# Configuramos una url para poder cargar imagenes
# Comprobamos que este en modo debugg
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
