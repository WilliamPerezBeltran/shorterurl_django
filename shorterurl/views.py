from django.shortcuts import render, get_object_or_404, redirect
import pdb
from .models import Url
import ast


def index(request):
    try:
        if request.method == "POST":
            url = request.POST["url"]
            url_base62 = Url.decode_url_string_to_base62("", url)
            if not isinstance(url_base62, Exception):
                object_url = Url.objects.create(url_text=url, url_base62=url_base62)
                host_name_of_my_app = request.META["HTTP_HOST"]

                context = {
                    "object_url": object_url,
                    "url_name": host_name_of_my_app + "/" + object_url.url_base62,
                }

                return render(request, "shorterurl/index.html", context)
            else:
                # pdb.set_trace()
                error = ast.literal_eval(str(url_base62))[0]
                context = {"error": error}
                return render(request, "shorterurl/index.html", context)

    except Exception as e:
        context = {"error": e}
        return render(request, "shorterurl/index.html", context)
    else:
        return render(request, "shorterurl/index.html",)


def redirect_url(request, shorter_url):
    try:
        get_url = Url.objects.filter(url_base62=shorter_url)[0]
    except Exception as e:
        return render(request, "shorterurl/page_not_Found.html",)
    else:
        return redirect(get_url.url_text)
