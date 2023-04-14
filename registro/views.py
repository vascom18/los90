from django.shortcuts import redirect, render


from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib import messages


class VRegistro(View):

    def get(self, request):
        form = UserCreationForm()

        ctx = {'form': form}

        return render(request, 'registro/registro.html', ctx)

    def post(self, request):

        form = UserCreationForm(request.POST)
        if form.is_valid():

            usuario = form.save()

            login(request, usuario)

            return redirect('home')

        else:

            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, 'home/index.html', {'form': form})


def salir(request):

    logout(request)

    return redirect('home')


def loginn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            pasw = form.cleaned_data.get('password')
            usuario = authenticate(username=name, password=pasw)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, 'usuario no valido')
        else:
            messages.error(request, 'informacion incorrecta')

    form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})
