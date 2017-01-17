from django.db import models
from django.core.urlresolvers import reverse
import django.utils.timezone as timezone
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)  # title
    category = models.CharField(max_length=50, blank=True)  # category
    date_time = models.DateTimeField('保存日期', default=timezone.now)  # time
    content = models.TextField(blank=True, null=True)   # content
    TYPE_CHOICES = (
        ('A', 'Audio'),
        ('V', 'Video'),
        ('I', 'Image'),
        ('S', 'Status'),
        ('B', 'Blog'),
        ('P', 'Project'),
    )
    post_type = models.CharField(max_length=2,choices=TYPE_CHOICES,default='B')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path
