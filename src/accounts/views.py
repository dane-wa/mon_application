from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms.CustomUserLoginForm import CustomUserLoginForm
from django.contrib import messages
# Create your views here.
def login_user(request):
    if request.method == "POST":
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('retraite:home')
            else:
                messages.error(request, "Nom d'utilisateur ou Mot de passe incorrect.")
        else:
            messages.error(request, "Nom d'utilisateur ou Mot de passe non valide.")
    else:
        form = CustomUserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})



def logout_user(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'accounts/logged_out.html')
