from django.views import generic
from django.shortcuts import render
from .models import Article, Worker, Moderator


def work_art_det(request, pk):
    article = Article.objects.get(pk=pk) # order_by('id')[pk-1]
    worker = article.author  #Worker.objects.filter(id=pk).prefetch_related('author')
    context = {'worker': worker,
               'article': article,
               }
    return render(request, 'article_detail.html', context)



class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['worker'] = Worker.objects.all()
        return context
