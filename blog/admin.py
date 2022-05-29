from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.Worker)
admin.site.register(models.Moderator)
admin.site.register(models.Article, ArticleAdmin)

# Register your models here.
