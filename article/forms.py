from django.forms import ModelForm
from . import models

class ArticleForm(ModelForm):

	class Meta:
		model = models.ArticleModel
		fields = ["title_text", 'article_text']