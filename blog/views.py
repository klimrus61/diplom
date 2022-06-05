from django.views import generic
from .models import Article, Worker, Moderator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def worker_detail(request, pk):
    worker = get_object_or_404(Worker, pk=pk) # Article.objects.get(pk=pk) # order_by('id')[pk-1]
    context = {'worker': worker,
               }
    return render(request, 'blog/worker_detail.html', context)


class AddWorkerView(generic.CreateView):
    model = Worker
    template_name = 'blog/add_worker.html'
    fields = ['full_name', 'user', 'trail', 'work_post', 'tabel_num', 'hired', 'order_num']


class AddArticleView(generic.CreateView):
    model = Article
    template_name = 'blog/add_article.html'
    fields = ['title', 'author', 'price', 'text_b', 'trips_num', 'data_per_1', 'data_per_2']


def article_list(request):
    article_zero = Article.objects.filter(status=0, author_id=request.user.id).order_by('-created_on')
    article_list_check = Article.objects.filter(status=1, author_id=request.user.id).order_by('-created_on')
    article_error = Article.objects.filter(status=2, author_id=request.user.id).order_by('-created_on')
    context = {
        'article_list': article_zero,
        'article_list_check': article_list_check,
        'article_list_error': article_error,

    }
    return render(request, 'index.html', context)


def work_art_det(request, pk):
    article = get_object_or_404(Article, pk=pk) # Article.objects.get(pk=pk) # order_by('id')[pk-1]
    worker = article.author  #Worker.objects.filter(id=pk).prefetch_related('author')
    #if worker.user == User:
    user_now = worker.user
    context = {'worker': worker,
               'article': article,
               'user_now': user_now,
               }
    return render(request, 'article_detail.html', context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="blog/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="blog/login.html", context={"login_form": form})


#class ArticleList(generic.ListView):
#    queryset = Article.objects.filter(status=1, ).order_by('-created_on')
#    template_name = 'index.html'




class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['worker'] = Worker.objects.all()
        return context
