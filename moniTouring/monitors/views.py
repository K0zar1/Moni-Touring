from django.shortcuts import render

# Create your views here.


def monitor_add(request):
    return render(request, 'monitors/monitor-add-page.html')


def monitor_details(request, username, monitor_name):
    return render(request, 'monitors/monitor-details-page.html')


def monitor_edit(request, username, monitor_name):
    return render(request, 'monitors/monitor-edit-page.html')


def monitor_delete(request, username, monitor_name):
    return render(request, 'monitors/monitor-delete-page.html')