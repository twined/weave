from django import template

from posts.models import Post

register = template.Library()


@register.inclusion_tag('posts/templatetags/latest_posts_overview.html',
        takes_context=True)
def latest_posts_overview(context):
    """
    Renders latest posts overview
    """

    news_posts = Post.latest.news_posts()
    blog_posts = Post.latest.blog_posts()

    return {
        'news_posts': news_posts,
        'blog_posts': blog_posts,
    }
