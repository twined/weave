# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView

from .models import Post
from hiver.decorators import cache_page

CACHE_TIME = 60 * 60
cache_post = method_decorator(cache_page(CACHE_TIME,
    '{{ project_name }}.posts.view'))


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/detail.html"

    def get_queryset(self):
        return Post.published.all().filter(
                slug__iexact=self.kwargs['slug'],
                post_type=self.kwargs['post_type'])

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.latest.news_posts(count=10) \
            if self.kwargs['post_type'] == 0 else Post.latest.blog_posts(count=10)
        context['post_type'] = self.kwargs['post_type']
        return context

    @cache_post
    def dispatch(self, *args, **kwargs):
        return super(PostDetailView, self).dispatch(*args, **kwargs)


@cache_page(CACHE_TIME, '{{ project_name }}.posts.news.list')
def list_news(request):
    posts = Post.published.all().filter(post_type=Post.PT_NEWS).order_by('-pk')
    return render(request, 'posts/list.html', {
        'posts': posts,
        'post_type': Post.PT_NEWS
    })


@cache_page(CACHE_TIME, '{{ project_name }}.posts.blog.list')
def list_blogposts(request):
    posts = Post.published.all().filter(post_type=Post.PT_BLOG).order_by('-pk')
    return render(request, 'posts/list.html', {
        'posts': posts,
        'post_type': Post.PT_BLOG
    })
