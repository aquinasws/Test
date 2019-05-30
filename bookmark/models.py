from django.db import models

# Create your models here.

from django.urls import reverse
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('site URL')

    def __str(self):
        return "Name: " + self.site_name + ", URL: " + self.url

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])







