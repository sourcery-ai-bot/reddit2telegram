#encoding:utf-8

from utils import get_url
from utils import SupplyResult


subreddit = 'chemicalreactiongifs'
t_channel = '@r_chemicalreactiongifs'
footer = 'by {}'.format(t_channel)


def send_post(submission, r2t):
    what, url, ext = get_url(submission)
    title = submission.title
    link = submission.shortlink
    text = '{}\n{}\n\n{}'.format(title, link, footer)
    if what == 'gif' and r2t.dup_check_and_mark(url) is True or what != 'gif':
        return SupplyResult.DO_NOT_WANT_THIS_SUBMISSION
    else:
        return r2t.send_gif_img(what, url, ext, text)
