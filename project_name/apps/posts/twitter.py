'''
from twython import Twython
from twython.twython import TwythonError
from django.conf import settings
from django.contrib import messages


def post_to_twitter(request, post):
    try:
        t = Twython(app_key=settings.TWYTHON['app_key'],
                    app_secret=settings.TWYTHON['app_secret'],
                    oauth_token=settings.TWYTHON['oauth_token'],
                    oauth_token_secret=settings.TWYTHON['oauth_token_secret'])
        t.updateStatus(status="from {{ project_name }} // %s %s" %
            (post.header, request.build_absolute_uri(post.get_absolute_url())))

    except TwythonError, e:
        messages.error(request, "Twitter feil! %s: %s" % (e.error_code, e.msg), extra_tags='msg')
        return False

    messages.success(request, "Postet til twitter!", extra_tags='msg')
    post.tweeted = True
    post.save()
    return True
'''
