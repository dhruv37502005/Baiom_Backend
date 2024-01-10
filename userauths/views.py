from django.shortcuts import redirect, render
from .form import UseRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model

User = settings.AUTH_USER_MODEL


# email verfication
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)


account_activation_token = AccountActivationTokenGenerator()


def signup(request):
    if request.method == 'POST':
        form = UseRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully.")

            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
            })
            to_email = form.cleaned_data.get('email')

            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.content_subtype = 'html'
            email.send()

            messages.success(request, "Please confirm your email address to complete the registration")
            
    else:
        form = UseRegisterForm()

    context = {'form': form}
    return render(request, 'signup.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_superuser == True:
                login(request, user)
                return redirect('dashboard:admin_ui')
            else:
                login(request, user)
                request.session['username'] = user.username
                return redirect('core:index')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('userauths:login')
    else:
        return render(request, 'login.html')


# def login_view(request):
#     print("Done")
#     if request.user.is_authenticated:
#
#         messages.warning(request, f"You are already logged in as {request.user.username}")
#
#     if request.method == 'POST':
#         print("InsidePost")
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         try:
#             user = User.objects.get(email=email)
#
#         except:
#             messages.warning(request, f"User with {email} does not exist")
#
#         user = authenticate(request, email=email, password=password)
#
#         if user is not None:
#             print("Inside if")
#             login(request, user)
#             messages.success(request, f"Welcome back {user.username}")
#             return redirect("core:index")
#         else:
#             messages.warning(request, f"User does not exist, create an account.")
#
#     context = {
#         'title': 'Login',
#     }
#
#     return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")

    return redirect("core:index")


def home(request):
    return render(request, "home.html")


# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         # Activate the user account
#         user.is_active = True
#         user.save()

#         # Redirect to the login page
#         return redirect('userauths:login')
#     else:
#         return HttpResponse('Activation link is invalid!')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # Activate the user account
        user.is_active = True
        user.save()
        # Redirect to the login page
        return redirect('userauths:login')
    else:
        return HttpResponse('Activation link is invalid!')


