from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.article_list, name='home'),

    path("add_worker/", views.AddWorkerView.as_view(), name="add_worker"),
    #path('', views.ArticleList.as_view(), name='home'),
    path('blog/<int:pk>/', views.work_art_det, name='article_detail'),
    path("register/", views.register_request, name="register"),
    #path("login/", views.login_request, name="login"),
    path("add_article/", views.AddArticleView.as_view(), name='add_article'),
    path("worker_detail/<int:pk>/", views.worker_detail, name='worker_detail'),
]
#     path('<int:pk>/', views.ArticleDetail.as_view(), name='article_detail'),