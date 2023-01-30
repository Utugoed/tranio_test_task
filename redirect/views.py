from django.shortcuts import render, redirect

from shorter.models import ShortUrl


def get_redirect_url(request, code: str):
    short_url_set = ShortUrl.objects.all().filter(code=code)
    if short_url_set:
        short_url = short_url_set[0]
        short_url.update_counter()
        return redirect(short_url.url)
    return render(request, '404.html')
