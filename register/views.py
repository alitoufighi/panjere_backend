from django.shortcuts import render, redirect
from .forms import RegistrationForm
import csv
from django.http import HttpResponse
from .models import Attendant


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


def export_attendants_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'first_name',
        'last_name',
        'email',
        'major',
        'university',
        'registration_time'
    ])

    attendants = Attendant.objects.all().values_list(
        'first_name',
        'last_name',
        'email',
        'major',
        'university',
        'registration_time'
    )

    for team in attendants:
        writer.writerow(team)

    return response
