from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from moniTouring.common.forms import SearchForm
from moniTouring.monitors.models import Monitor


# Create your views here.


def index(request):
    all_monitors = Monitor.objects.all()
    search_form = SearchForm()
    user = request.user

    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_monitors = all_monitors.filter(name=search_form.cleaned_data['search'])

    context = {
        "all_monitors": all_monitors,
        "search_form": search_form,
        "user": user,
    }
    return render(request, 'common/home-page.html', context)


def share_link(request, monitor_name):
    copy(request.META['HTTP_HOST'] + resolve_url('monitor details', monitor_name))

    return redirect(request.META['HTTP_REFERER'] + f"#{monitor_name}")