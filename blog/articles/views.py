from django.shortcuts import render
from django.http import Http404
from .models import Lease


def archive(request):
    return render(request, 'archive.html', {"posts": Lease.objects.all()})


def get_lease(request, lease_id):
    try:
        post = Lease.objects.get(id=lease_id)
        return render(request, 'lease.html', {"post": post})
    except Lease.DoesNotExist:
        raise Http404
