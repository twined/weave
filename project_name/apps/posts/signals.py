from django.core.cache import cache


def invalidate_cache(sender, **kwargs):
    # invalidate homepage
    cache.delete_pattern('{{ project_name }}.pages.home/*')
    cache.delete_pattern('{{ project_name }}.posts.view/*')
    cache.delete_pattern('{{ project_name }}.posts.blog.list/*')
    cache.delete_pattern('{{ project_name }}.posts.news.list/*')
