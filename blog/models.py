from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager


class Contact(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)

    def _str_(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])

    class Meta:  # include this to ensure build in IDE
        app_label = "blog"


class Post(models.Model):
    author = models.ForeignKey('account.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

class ViewsSummary(Post):
    class Meta:
        proxy = True
        verbose_name = "View Summary"
        verbose_name_plural = "View Summary"