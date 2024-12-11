from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from moniTouring.common.forms import *
from moniTouring.monitors.models import Monitor
from moniTouring.common.models import Review


# Create your views here.


def index(request):
    all_monitors = Monitor.objects.all()
    review_form = ReviewForm()
    search_form = SearchForm()
    user = request.user

    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_monitors = all_monitors.filter(name=search_form.cleaned_data['search'])

    context = {
        "all_monitors": all_monitors,
        "review_form": review_form,
        "search_form": search_form,
        "user": user,
    }
    return render(request, 'common/home-page.html', context)


def add_review(request, monitor_id):
    monitor = Monitor.objects.get(id=monitor_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.to_monitor = monitor
            review.user = request.user
            review.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{monitor_id}")


@login_required
def review_edit(request, review_id, monitor_name):
    review = Review.objects.get(id=review_id)

    if request.method == "GET":
        form = ReviewEditForm(instance=review, initial=review.__dict__)
    else:
        form = ReviewEditForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('monitor details', monitor_name)
    context = {"form": form}

    return render(request, 'common/review-edit-page.html', context)


@login_required
def review_delete(request, review_id, monitor_name):
    review = Review.objects.filter(id=review_id).first()
    monitor = Monitor.objects.filter(slug=monitor_name).first()
    user = review.user
    if request.method == 'POST':
        review.delete()
        return redirect('monitor details', monitor_name)
    form = ReviewDeleteForm(initial=review.__dict__)
    context = {"review": review, "form": form, "monitor": monitor, "user": user}
    return render(request, 'common/review-delete-page.html', context)