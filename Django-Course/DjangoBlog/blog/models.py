from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


# Create your models here.
# CLASS USER
class User(AbstractUser):
    class Meta:
        db_table = "users"

    def __str__(self):
        mssg = "(admin)" if self.is_superuser else ""
        return f"{self.username} {mssg}"


# CLASS CATEGORY
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = "categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


# CLASS ARTICLE
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField(upload_to="articles/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    categories = models.ManyToManyField(Category, related_name="articles")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "articles"

    def __str__(self):
        mssg = "(public)" if self.is_published else "(private)"
        return f"{self.title} {mssg}"
