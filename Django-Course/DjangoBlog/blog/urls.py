from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/", views.blog, name="blog"),
    path("blog/<slug:slug>", views.blog, name="blog_category"),
    path("article/<int:pk>", views.article, name="article"),
]

# Solo para el entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
