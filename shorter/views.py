from django.shortcuts import render

from shorter.forms import UrlForm
from shorter.models import ShortUrl

# Create your views here.
def get_index_page(request):
    return render(request, "shorter/index.html")


def create_code(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            short_url = ShortUrl.create_code(url=url)
            return render(
                request,
                "shorter/code_created.html",
                {
                    "short_url": short_url
                }
            )
        else:
            return render(
                    request,
                    'shorter/create_code.html',
                    {
                        'form': form,
                        'error_message': 'Input should be a valid URL'
                    }
                ) 
    elif request.method == 'GET':
        form = UrlForm()
        return render(request, 'shorter/create_code.html', {'form': form, 'error_message': None})


def statistic(request):
    urls = ShortUrl.objects.all()
    return render(request, "shorter/statistic.html", {"urls": urls})