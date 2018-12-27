from django.shortcuts import render, redirect
from .forms import RegistrationForm


def accept(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            error = {'error': None}
            return render(request, 'done.html', error)
        else:
            error = {"error": form.errors}
            return render(request, 'done.html', error)
    return redirect('home.html')
