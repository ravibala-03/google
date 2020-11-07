from django.db import models

from django.db import models


class SearchResult(models.Model):

    urls = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

