from django.shortcuts import redirect, render
from userauths.form import UseRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL


def signup(request):
    if request.method == 'POST':
        form = UseRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully.")

            authenticated_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )

            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect("core:index")
            else:
                # Handle authentication failure, e.g., display an error message
                messages.error(request, "Authentication failed.")

    else:
        form = UseRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in as {request.user.username}")

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

        except:
            messages.warning(request, f"User with {email} does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back {user.username}")
            return redirect("core:index")
        else:
            messages.warning(request, f"User does not exist, create an account.")

    context = {
        'title': 'Login',
    }

    return render(request, 'login.html', context , )


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")

    return redirect("core:index")
