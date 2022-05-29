from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify  # new
from django.urls import reverse


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Moderator(models.Model):
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class Worker(models.Model):
    full_name = models.CharField(max_length=100)
    trail = models.CharField(max_length=255)
    work_post = models.CharField(max_length=20)
    tabel_num = models.CharField(max_length=20)
    hired = models.DateField()
    order_num = models.CharField(max_length=20)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('worker_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new auto slug outside admin.py
        if not self.slug:
            self.slug = slugify(self.full_name)
        return super().save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    created_on = models.DateField(auto_now=True, editable=True)
    text_b = models.TextField(blank=True, null=True, help_text='Введите номера билетов')
    trips_num = models.DecimalField(max_digits=2, decimal_places=0)  #Кол во поездок
    num_days_worked = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    day_verify = models.DateField(blank=True, null=True)  # day checks
    author = models.ForeignKey(Worker, on_delete=models.CASCADE)
    pers_check = models.ForeignKey(Moderator, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
