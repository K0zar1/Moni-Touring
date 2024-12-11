from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from moniTouring.common.forms import ReviewForm
# from moniTouring.common.forms import CommentForm
# from moniTouring.common.models import Comment
from moniTouring.monitors.forms import MonitorAddForm, MonitorDeleteForm, MonitorEditForm
from moniTouring.monitors.models import Monitor


@login_required
def monitor_add(request):
    form = MonitorAddForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        monitor = form.save(commit=False)
        monitor.user = request.user
        monitor.save()
        return redirect('index')

    context = {"form": form}
    return render(request, 'monitors/monitor-add-page.html', context)


def monitor_details(request, monitor_name):
    monitor = Monitor.objects.filter(slug=monitor_name).first()
    reviews = monitor.review_set.all()
    review_form = ReviewForm()

    context = {
        "monitor": monitor,
        "reviews": reviews,
        "review_form": review_form,
    }

    return render(request, 'monitors/monitors-details-page.html', context)


@login_required
def monitor_edit(request, monitor_name):
    monitor = Monitor.objects.get(slug=monitor_name)

    if request.method == "GET":
        form = MonitorEditForm(instance=monitor, initial=monitor.__dict__)
    else:
        form = MonitorEditForm(request.POST, request.FILES, instance=monitor)
        if form.is_valid():
            form.save()
            return redirect('monitor details', monitor_name)
    context = {"form": form}

    return render(request, 'monitors/monitor-edit-page.html', context)


@login_required
def monitor_delete(request, monitor_name):
    monitor = Monitor.objects.filter(slug=monitor_name).first()
    if request.method == 'POST':
        monitor.delete()
        return redirect('index')
    form = MonitorDeleteForm(initial=monitor.__dict__)
    context = {"monitor": monitor, "form": form, "monitor_name": monitor_name}
    return render(request, 'monitors/monitor-delete-page.html', context)