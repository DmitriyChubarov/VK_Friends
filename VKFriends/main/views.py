from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def main(request):
    users = User.objects.exclude(id=request.user.id)

    context = {
        'users': users
    }

    return render(request, 'main/home.html', context)


