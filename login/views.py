from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Cambia 'home' al nombre de la vista a la que quieres redirigir después del login
        else:
            # Manejar el caso en que las credenciales no sean válidas
            pass

    return render(request, 'login/login.html')  # Crea este archivo HTML en el directorio templates/login_rrss/

def logout_view(request):
    logout(request)
    return render(request, 'login/logout.html')  # Ruta actualizada


def home_view(request):
    return render(request, 'login/home.html')  