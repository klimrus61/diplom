from django.views import generic
from .models import Article, Worker, Moderator


class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'article_detail.html'

