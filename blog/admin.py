from django.contrib import admin
from . import models


admin.site.register(models.Article)
admin.site.register(models.Worker)
admin.site.register(models.Moderator)

# Register your models here.
