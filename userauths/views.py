from django.shortcuts import redirect, render
from userauths.form import UseRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UseRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect("core:index")
    else:
        print("user cannot be registered")
        form = UseRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)

# Rename the login function to login_view to avoid conflicts
def login_view(request):
    return render(request, 'login.html')


