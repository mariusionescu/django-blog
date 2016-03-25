from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from blog.models import Post


if 'cms' in settings.INSTALLED_APPS:
    from cms.models import Page
    CMS = True
else:
    CMS = False


class BlogView(View):

    def get(self, request):
        search = request.GET.get('q')
        page_number = request.GET.get('p', 0)

        language = request.path.split('/')[1]
        available_languages = [l[0] for l in Post.LANGUAGES]
        language = language if language in available_languages else 'ro'

        context = {}
        if CMS:
            try:
                if request.user.is_authenticated():
                    page = Page.objects.get(path=request.path)
                else:
                    page = Page.objects.get(path=request.path, published=True)
            except Page.DoesNotExist:
                pass
            else:
                for placeholder in page.placeholder_set.all():
                    context[placeholder.name] = placeholder.content

        if request.user.is_authenticated():
            qs = Post.objects.filter(language=language).order_by('-date_created')
            if search:
                qs = qs.filter(language=language, content__contains=search)
            context['posts'] = qs[page_number*10:page_number+10]
        else:
            qs = Post.objects.filter(language=language, published=True).order_by('-date_created')
            if search:
                qs = qs.filter(language=language, content__contains=search)
            context['posts'] = qs[page_number*10:page_number+10]
        context['path'] = request.path
        return render(request, 'blog.html', context)


class PostView(View):

    def get(self, request, slug):
        context = {}
        if CMS:
            try:
                if request.user.is_authenticated():
                    page = Page.objects.get(path=request.path)
                else:
                    page = Page.objects.get(path=request.path, published=True)
            except Page.DoesNotExist:
                pass
            else:
                for placeholder in page.placeholder_set.all():
                    context[placeholder.name] = placeholder.content

        if request.user.is_authenticated():
            post = Post.objects.get(slug=slug)
            recent_posts = Post.objects.all().order_by('-date_created')[:3]
        else:
            post = Post.objects.get(slug=slug, published=True)
            recent_posts = Post.objects.filter(published=True).order_by('-date_created')[:3]

        context['path'] = request.path
        context['page_title'] = post.title
        context['post'] = post
        context['body_class'] = 'blog-page blog-single'
        context['recent_posts'] = recent_posts
        return render(request, 'post.html', context)
