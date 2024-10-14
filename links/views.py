from django.shortcuts import get_object_or_404, redirect, render

from .forms import LinkForm
from .models import Link


# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        "links": links,
    }
    return render(request, "links/index.html", context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()  # increment click field by 1
    return redirect(link.url)


def add_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            # process the data
            print(form.cleaned_data)
        else:
            form = LinkForm()
    context = {
        "form": form,
    }
    return render(request, "links/add_link.html", context)
