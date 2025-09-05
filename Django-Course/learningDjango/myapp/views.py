from django.shortcuts import render, HttpResponse, redirect

# from django.db.models import Q
from django.contrib import messages
from myapp.models import Article
from myapp.forms import FormArticle

# from django.db.models import Q


# Create your views here.

# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista --> Acciones (metodos)

# Layout para navegar por las paginas
LAYOUT = """
    <h1>Web Site with Django | Víctor Muntané </h1>
    <hr/>
    <ul>
        <li>
            <a href="/home">Home</a>
        </li>
        <li>
            <a href="/hello-world">Hello World</a>
        </li>
        <li>
            <a href="/test-page">Test Page</a>
        </li>
        <li>
            <a href="/contact">Contact</a>
        </li>
    </ul>
    <hr/>
"""


# Usamos una template separada de la vista creando un fichero template en nuestra app
def index(request):
    year = 2025
    until = range(year, 2051)
    name = "Victor Muntane"
    languages = ["Javascript", "Pyhton", "PHP", "C"]

    return render(
        request,
        "index.html",
        {
            "title": "Home",
            "my_variable": "I am a data that is in the view",
            "name": name,
            "languages": languages,
            "years": until,
        },
    )


def hello_world(request):
    return render(request, "hello-world.html")


# Redirigimos la pagina a otro lado dependiendo si introducimos un valor o otro en la url
def page(request, redirect_url=0):
    if redirect_url == 1:
        return redirect("contact", name="Victor", surname="Muntane")
    else:
        return render(
            request, "page.html", {"text": "", "list": ["one", "two", "three"]}
        )


def contact(request, name="", surname=""):
    html = "<p>The full name is:</p>"
    if name and surname:
        html += f"<h3>{name} {surname}</h3>"
    return HttpResponse(LAYOUT + "<h2>Contact</h2>" + html)


# Creamos una vista para crear un articulo
def create_article(request, title, content, public):
    article = Article(title=title, content=content, public=public)
    article.save()
    return HttpResponse(
        f"Article Created: <strong>{article.title}</strong> - {article.content}"
    )


# Crear un articulo mediante form
def save_article(request):

    if request.method == "POST":
        # Recogemos los datos que nos llegan por POST
        title = request.POST.get("title")
        content = request.POST.get("content")
        public = request.POST.get("public")
        article = Article(title=title, content=content, public=public)
        article.save()
        return HttpResponse(
            f"Article Created: <strong>{article.title}</strong> - {article.content}"
        )
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo </h2>")


def create_article_form(request):
    return render(request, "create_article.html")


# Creamos formularios a raiz delo objeto forms
def create_full_article(request):

    if request.method == "POST":
        form = FormArticle(request.POST)
        if form.is_valid():
            form.save()
            # crear mensaje flash (sesion que solo se muestra 1 vez)
            messages.success(request, "Article has been created successfully")
            return redirect("articles")
    else:
        form = FormArticle()
    return render(request, "create_full_article.html", {"form": form})


# Extraer informacion tabla BBDD
def show_article(request):
    try:
        article = Article.objects.get(id=1)
        response = f"Article: <br/> {article.pk}. {article.title}"
    except Article.DoesNotExist:
        response = "<h1>Article not found</h1>"
    return HttpResponse(response)


# Actualizar informacion BBDD
def update_article(request, id_article):
    article = Article.objects.get(pk=id_article)
    article.title = "Batman"
    article.content = "Film from 2017"
    article.public = False
    article.save()
    return HttpResponse(
        f"<h1>Article {article.pk} Updated</h1> <br/>{article.title} - {article.content}"
    )


# Mostrar listado de articulos
def articles_list(request):
    # Sacamos todo el contenido de la lista
    # articles = Article.objects.all().order_by("-pk")

    # Podemos ordenar las listas por algun argumento o limitar cuantod queremos mostrar
    # articles = Article.objects.order_by("pk")[0:3]

    # Sacamos el contenido con filtros
    # articles = Article.objects.filter(title="First Article", pk=1)

    # Trabajamos con lookups
    # articles = Article.objects.filter(title__contains="article")

    # Saca el contenido exacto sin keysensitive
    # articles = Article.objects.filter(title__iexact="article")

    # Sacar articulos cuyo pk o id sea mayor(gt) o igual (gte) o menores(lt - lte) a 12
    # articles = Article.objects.filter(pk__lte=7)

    # Articulos que sea articulo pero que solo saque los que estan publicados usando exclude
    # articles = Article.objects.filter().exclude(public=False)

    # Sacamos solo los cmapos que nos interesen
    # articles = Article.objects.values('title')

    # Usamos consultas SQL tipicas
    # articles = Article.objects.raw("SELECT * FROM myapp_article WHERE title = 'First Article'")

    # Sacar articulo que cumplan una condicion o otra
    # articles = Article.objects.filter(Q(pk=8) | Q(title__contains="First"))

    articles = Article.objects.filter(public=1)
    return render(request, "articles.html", {"articles": articles})


# Eliminar articulo
def delete_article(request, id_article):
    article = Article.objects.get(pk=id_article)
    article.delete()
    return redirect("articles")
