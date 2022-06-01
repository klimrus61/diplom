from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<int:pk>/', views.work_art_det, name='article_detail'),

]
#     path('<int:pk>/', views.ArticleDetail.as_view(), name='article_detail'),