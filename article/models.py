from django.db import models
from markdownx.models import MarkdownxField
import datetime 
from django.template.defaultfilters import slugify
from markdownx.utils import markdownify

from django.contrib.auth.models import User

# Create your models here.
class ArticleModel(models.Model):
    """
    Description: Model Description
    """
    title_text = models.CharField(max_length=1000, blank=False, null = False, default="")
    author_text = models.ForeignKey(User, on_delete=models.CASCADE)
    article_text = MarkdownxField()
    published_date = models.DateField(auto_now=True)
    slug_title_text = models.SlugField(editable=False, unique=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.article_text)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug_title_text = slugify(self.title_text)
            self.published_date = datetime.datetime.now().date()

        super(ArticleModel, self).save(*args, **kwargs)


    class Meta:
        unique_together = ('title_text', 'author_text', 'published_date')
   