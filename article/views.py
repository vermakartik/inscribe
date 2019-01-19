from django.shortcuts import render, get_object_or_404, reverse
from . import forms
from django.http import HttpResponseRedirect

from .models import ArticleModel
from django.views import generic

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def article_editor(request):
	if request.method == "POST":
		article_edit_form = forms.ArticleForm(request.POST)
		if article_edit_form.is_valid():
			article_object = article_edit_form.save(commit=False)
			article_object.author_text = request.user
			article_object.save()
			return HttpResponseRedirect(reverse('article:details', args=(article_object.published_date, article_object.slug_title_text)))
	article_edit_form = forms.ArticleForm(label_suffix="")
	print(article_edit_form)
	return render(request, 'article/new.html', {"form" : article_edit_form, 'new_article_button': False})

class ArticleList(generic.ListView):
	model = ArticleModel
	template_name = "article/list.html"

def detail_view(request, pub_date, article_name):
	article_object = get_object_or_404(ArticleModel, published_date = pub_date, slug_title_text = article_name)
	return render(request, "article/details.html", {'article_object': article_object})

def article_edit_article(request, pub_date, article_name):
	article_object = get_object_or_404(ArticleModel, published_date = pub_date, slug_title_text = article_name)
	if request.method == "POST":
		article_form = forms.ArticleForm(request.POST, instance=article_object)
		if article_form.is_valid():
			article_object_new = article_form.save()
			return HttpResponseRedirect(reverse('article:details', args=(article_object_new.published_date, article_object_new.slug_title_text)))
	article_form = forms.ArticleForm(instance = article_object)
	return render(request, "article/edit.html", { "form": article_form })


