from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):

    LANGUAGES = (
        ('ro', 'RO'),
        ('en', 'EN')
    )
    title = models.CharField(max_length=2048, null=False, blank=False, default="Blog Title")
    content = models.TextField()
    date_created = models.DateField(default=timezone.now)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, null=True)
    slug = models.CharField(max_length=2048, null=True, blank=True)
    language = models.CharField(max_length=8, null=False, blank=False, choices=LANGUAGES, default='ro')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

