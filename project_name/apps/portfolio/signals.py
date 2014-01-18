from django.core.cache import cache


def invalidate_portfolio_cache(sender, **kwargs):
    cache.delete_pattern('portfolio.*')
