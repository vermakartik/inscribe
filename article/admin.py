from django.contrib import admin

# Register your models here.
from markdownx.admin import MarkdownxModelAdmin
from . import models

admin.site.register(models.ArticleModel, MarkdownxModelAdmin)

