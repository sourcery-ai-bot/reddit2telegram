#encoding:utf-8

from urllib.parse import urlparse

from utils import get_url
from utils import SupplyResult


t_channel = '@OldSchoolCool'
subreddit = 'OldSchoolCool'


def send_post(submission, r2t):
    what, url, ext = get_url(submission)
    title = submission.title
    link = submission.shortlink
    text = '{}\n{}'.format(title, link)

    if (
        what == 'text'
        or what == 'album'
        or what not in ('other', 'gif', 'img')
    ):
        return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
    elif what == 'other':
        domain = urlparse(url).netloc
        if domain in ('www.youtube.com', 'youtu.be'):
            text = '{}\n{}\n\n{}'.format(title, url, link)
            return r2t.send_text(text)
        else:
            return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
    else:
        return r2t.send_gif_img(what, url, ext, text)
