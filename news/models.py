from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50, default='news-title')
    text = models.TextField(blank=True, null=True, default='news')
    image = models.FileField(upload_to='media/', blank=True, null=True)
    video = models.FileField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title
