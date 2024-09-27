from django.shortcuts import get_object_or_404, render

from .models import Shahid


def shahid_list(request):
    shahids = Shahid.objects.all()

    return render(request, "shahid/list.html", {"shahid_list": shahids})


def shahid_detail(request, slug):
    shahid = get_object_or_404(Shahid, slug=slug)
    return render(request, "shahid/detail.html", {"shahid": shahid})
