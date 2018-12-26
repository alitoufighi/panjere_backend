from django.shortcuts import render
from .forms import RegistrationForm


def accept(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            error = {'error': None}
            return render(request, 'done.html', error)
        else:
            # print(form.errors.items())
            if 'name' in form.errors.items():
                print("Name Error", form.errors['name'])
                error = {'name': form.errors['name']}
            else:
                print("Error!")
                error = {'error': True}
            print(error)
            return render(request, 'done.html', error)

    return render(request, 'home.html')
