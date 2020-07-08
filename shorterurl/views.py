from django.shortcuts import render, get_object_or_404, redirect
import pdb
from .models import Url


def index(request):
    try:
        if request.method == "POST":

            url = request.POST["url"]
            try:
                url_base62 = Url.decode_url_string_to_base62("", url)
            except Exception as e:
                context = {"error": e}
            else:
                object_url = Url.objects.create(url_text=url, url_base62=url_base62)
                host_name_of_my_app = request.META["HTTP_HOST"]

                context = {
                    "object_url": object_url,
                    "url_name": host_name_of_my_app + "/" + object_url.url_base62,
                }
                return render(request, "shorterurl/index.html", context)

    except Exception as e:
        context = {"error": e}
        return render(request, "shorterurl/index.html", context)
    else:
        return render(request, "shorterurl/index.html",)


def redirect_url(request, shorter_url):

    get_url = Url.objects.filter(url_base62=shorter_url)[0]

    return redirect(get_url.url_text)
