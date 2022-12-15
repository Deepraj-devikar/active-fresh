from django.shortcuts import redirect
from .models import *

def save_info(request, *args, **kw_args):
    if request.method == 'POST':
        Info.objects.create(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        return redirect('/contact')
