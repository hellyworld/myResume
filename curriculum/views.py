from django.shortcuts import render
from curriculum.models import Experience


def home(request):
    all_experiences = Experience.objects.order_by("-id")
    context = {
        'all_experiences': all_experiences,
    }

    return render(request, 'base.html', context)
