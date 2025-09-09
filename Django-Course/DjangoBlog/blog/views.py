from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category


# Create your views here.
def home(request):
    articles = (
        Article.objects.prefetch_related("categories")
        .filter(is_published=True)
        .order_by("-updated_at")[:3]
    )
    return render(request, "home.html", {"articles": articles})


def blog(request, slug=None):
    categories = Category.objects.all()
    articles = Article.objects.filter(is_published=True).order_by("-updated_at")

    cat_active = None
    if slug:
        cat_active = get_object_or_404(Category, slug=slug)
        articles = Article.objects.filter(
            categories__name=cat_active.name, is_published=True
        ).order_by("-updated_at")

    return render(
        request,
        "blog.html",
        {
            "categories": categories,
            "articles": articles,
            "cat_active": cat_active,
        },
    )


def article(request, pk):
    categories = Category.objects.all()
    article_obj = Article.objects.get(pk=pk)
    articles = (
        Article.objects.filter(is_published=True)
        .exclude(pk=pk)
        .order_by("-updated_at")[:3]
    )
    return render(
        request,
        "article.html",
        {"article": article_obj, "articles": articles, "categories": categories},
    )
