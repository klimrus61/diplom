from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


class WorkerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('full_name',), }


admin.site.register(models.Worker, WorkerAdmin)
admin.site.register(models.Moderator)
admin.site.register(models.Article, ArticleAdmin)

# Register your models here.
