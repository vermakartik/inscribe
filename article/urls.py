from django.urls import path

from . import views

app_name = "article"
urlpatterns = [
	path('new/', views.article_editor, name="new"),
	path("edit/<slug:pub_date>/<slug:article_name>/", views.article_edit_article, name="edit"),
	path('list/', views.ArticleList.as_view(), name="list"),
	path("view/<slug:pub_date>/<slug:article_name>/", views.detail_view, name = "details"),
]