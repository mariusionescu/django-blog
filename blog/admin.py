from django.contrib import admin

from blog import models
from django.conf import settings


class PostAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.6.0/codemirror.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.6.0/mode/xml/xml.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.6.0/mode/htmlmixed/htmlmixed.min.js',
            settings.STATIC_URL + 'blog/js/post.js'
        )

        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.6.0/codemirror.min.css',
                'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.6.0/theme/ambiance.min.css',
                settings.STATIC_URL + 'blog/css/post.css'
            )
        }

    list_display = ('title', 'language', 'date_created', 'published')

admin.site.register(models.Post, PostAdmin)


