from django.shortcuts import redirect, reverse


def index(request):
    return redirect(reverse('products:list'))
